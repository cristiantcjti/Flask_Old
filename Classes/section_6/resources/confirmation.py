import traceback
from time import time


from flask import make_response, render_template
from flask_restful import Resource

from models.confirmation import ConfirmationModel
from models.user import UserModel
from default import Config as config
from schemas.confirmation import ConfirmationSchema
from libs.mailgun import MailGunException
from libs.strings import gettext

confirmation_schema = ConfirmationSchema()


class Confirmation(Resource):
    @classmethod
    def get(cls, confirmation_id: str):
        """Returns confirmation HTML page."""
        confirmation = ConfirmationModel.find_by_id(confirmation_id)

        if not confirmation:
            return {'message': gettext('confirmation_not_found')}, 404

        if confirmation.expired:
            return {'message': gettext('confirmation_link_expired')}, 400

        if confirmation.confirmed:
            return {'message': gettext('confirmartion_already_confirmed')}, 400

        confirmation.confirmed = True
        confirmation.save_to_db()

        headers = {"Content-Type": "text/html"}
        return make_response(
            render_template("confirmation_page.html", email=confirmation.user.email),
            200,
            headers,
        )


class ConfirmationByUser(Resource):
    @classmethod
    def get(cls, user_id: int):
        """Returns confirmations for a given user. Use for Testing."""
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": config.USER_NOT_FOUND}, 404

        return (
            {
                'current_time': int(time()),
                'confirmation': [
                    confirmation_schema.dump(each) 
                    for each in user.confirmation.order_by(ConfirmationModel.expire_at)
                ],
            },
            200,
        )
        

    @classmethod
    def post(cls, user_id: int):
        """Resends confirmation email"""
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": config.USER_NOT_FOUND}, 404

        try:
            confirmation = user.most_recent_confirmation
            if confirmation:
                if confirmation.confirmed:
                    return {"message": config.ALREADY_CONFIRMED}, 400
                confirmation.force_to_expire()
            
            new_confirmation = ConfirmationModel(user_id)
            new_confirmation.save_to_db()
            user.send_confirmation_email()
            return {"message": config.RESEND_SUCCESS}, 201
                   
        except MailGunException as err:
            return {"message": err.message}, 500
        
        except:
            traceback.print_exc()
            return {"message": config.RESEND_FAIL}, 500