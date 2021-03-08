# Local Flask Application
# Designed to be deployed on AWS
# Author: Ryan Schneider

# flask
from flask import Flask
from flask_restful import Resource, Api

# mongo
from pymongo import MongoClient

# Set up Mongo
client = MongoClient('localhost',27017)
db = client.news_database

app = Flask(__name__)
api = Api(app)

todos = {}

# Basic Put and Get functions
class SecureFileUploader(Resource):
    def read(self, todo_id):
        # pymongo performing a query from database
        return {'todo:id': todos[todo_id]}

    def update(self, todo_id):
        todos[todo_id] = request.form['data']
        # pymongo command updating database
        return {todo_id: todos[todo_id]}

    def userGen(self, todo_id):
        todos[todo_id] = request.form['data']
        # pymongo command creating a user account in database
        return {todo_id: todos[todo_id]}

    def create(self, todo_id):
        todos[todo_id] = request.form['data']
        # pymongo adding a document to database
        return {todo_id: todos[todo_id]}

api.add_resource(SecureFileUploader,'/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)



