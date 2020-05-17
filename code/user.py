import sqlite3 # import package sqlite3
from flask_restful import Resource, reqparse

class User: # create class User and able to use sqlite3
    def __init__(self,_id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username): #create method which is able to find users by find_by_username
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?" #check the database for the matching username and use only that database
        result = cursor.execute(query, username)
        row = result.fetchone() #select first row from the result
        if row:
            user = cls(*row) # those match user ID,username and password which are in each row
        else:
            user = None # incase there is no match

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query ="SELECT * FROM users WHERE id=?" # to enable search by id
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):

    praser = reqparse.RequestParser() # to enable praser to go through json file of request and check for username and password
    praser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    praser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.praser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "A user with this username already exists"}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)" # TO Stop auto incrementing
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
