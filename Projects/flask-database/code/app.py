from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemsList


app = Flask(__name__)
app.secret_key = 'cris'
api = Api(app)

jwt = JWT(app, authenticate, identity) # Create a /auth endpoint by itself.

api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(port=5000, debug=True)