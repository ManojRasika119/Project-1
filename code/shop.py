from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class list_items(Resource):
    def get(self, name):
        return {name : "book, bag, cat, mug, magazine"}

api.add_resource(list_items, '/<string:name>')

class price(Resource):
    def post(self, name):
        if name == "book" :
            return {"price" : "5.99"}

        elif name == "bag" :
            return {"price" : "15.99"}

        elif name == "cat" :
            return {"price" : "85.99"}

        elif name == "mug" :
            return {"price" : "10.99"}

        elif name == "magazine" :
            return {"price" : "45.99"}

    def put(self, name):
        if name == "book" :
            return {"price" : "10.99"}

        elif name == "bag" :
            return {"price" : "25.99"}

        elif name == "cat" :
            return {"price" : "95.99"}

        elif name == "mug" :
            return {"price" : "100.99"}

        elif name == "magazine" :
            return {"price" : "45.99"}


api.add_resource(price, '/price/<string:name>')

app.run(port=5000)
