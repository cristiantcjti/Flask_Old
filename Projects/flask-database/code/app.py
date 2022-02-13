from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'cris'
api = Api(app)

jwt = JWT(app, authenticate, identity) # Create a /auth endpoint by itself.

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be blank!"
    )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': f"An item with name {name} already exists."}, 400

        data = request.get_json()

        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201

    @jwt_required()
    def put(self, name):
        data = request.get_json()
        
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {"name": name, "price": data["price"]}
            items.append(item)
        else:
            item.update(data)
        return item

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'item deleted'}

class ItemsList(Resource):
    def get(self):
        return {"items": items}

api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemsList, '/items')

app.run(port=5000, debug=True)