from flask import Flask # to import relavant packages from relavant library
from flask_restful import Api
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity
from user import UserRegister # UserRegister is our Resource
from item import Item # to import Item file whice is newly created

app = Flask(__name__)
app.secret_key = 'ManojR'
api = Api(app)

jwt = JWT(app, authenticate, identity) #applying JWT authentication

api.add_resource(Item, '/item/<string:name>')

api.add_resource(UserRegister, '/register')#once POST method executed, UserRegister will be called and then it calls post method in user.py

app.run(port=5000, debug=True)
