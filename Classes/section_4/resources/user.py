import traceback
from flask_restful import Resource
from flask import request, make_response, render_template
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)
from models.user import UserModel
from schemas.user import UserSchema
from blocklist import BLOCKLIST
from default import Config as config
from libs.mailgun import MailGunException
user_schema = UserSchema()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if UserModel.find_by_username(user.username):
            return {"message": config.USER_ALREADY_EXISTS}, 400

        if UserModel.find_by_email(user.email):
            return {"message": config.EMAIL_ALREADY_EXISTS}, 400

        try:
            user.save_to_db()
            user.send_confirmation_email()
            return {"message": config.SUCCESS_REGISTER_MESSAGE}, 201
        except MailGunException as e:
            user.delete_from_db()
            return {"message": e.message}, 500
        except:
            traceback.print_exc()
            return {"message": config.FAILED_TO_CREATE}, 400


class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": config.USER_NOT_FOUND}, 404

        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": config.USER_NOT_FOUND}, 404

        user.delete_from_db()
        return {"message": config.USER_DELETED}, 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = user_schema.load(user_json, partial=('email',)) # partial=  ignores the field passed

        user = UserModel.find_by_username(user_data.username)

        if user and user_data.password == user.password:
            if user.activated:
                access_token = create_access_token(identity=user.id, fresh=True)
                refresh_token = create_refresh_token(user.id)
                return {"access_token": access_token, "refresh_token": refresh_token}, 200
            return {"message": config.NOT_CONFIRMED_ERROR.format(user.email)}, 400

        return {"message": config.INVALID_CREDENTIALS}, 401


class UserLogout(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        jti = get_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        user_id = get_jwt_identity()
        BLOCKLIST.add(jti)
        return {"message": config.USER_LOGGED_OUT.format(user_id)}, 200


class TokenRefresh(Resource):
    @classmethod
    @jwt_required(refresh=True)
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200


class UserConfirm(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": config.USER_NOT_FOUND}, 404
        
        user.activated = True
        user.save_to_db()   
        headers = {"Content-Type": "text/html"}     
        return make_response(render_template("confirmation_page.html", email=user.email), 200, headers)

