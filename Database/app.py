# Local Flask Application
# Designed to be deployed on AWS
# Author: Ryan Schneider

# flask
from flask import Flask
from flask_restful import Resource, Api

# mongo
from pymongo import MongoClient
client = MongoClient()

# Set up Mongo
client = MongoClient('localhost',27017)
db = client.news_database

app = Flask(__name__)
api = Api(app)

# Basic Put and Get functions
class SecureFileUploader(Resource):
    def get(self, todo_id):
        return {'todo:id': todos[todo_id]}
    
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(SecureFileUploader,'/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)



