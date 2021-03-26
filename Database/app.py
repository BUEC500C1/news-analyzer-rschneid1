# Local Flask Application
# Designed to be deployed on AWS
# Author: Ryan Schneider

# flask
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
import mongoengine as me

# PyMongo Test
#from pymongo import MongoClient
#client = MongoClient('localhost',27017)
#db = client.news_database

app = Flask(__name__)
api = Api(app)

# Using MongoEngine
app.config['MONGODB_SETTINGS'] = {
    'db': 'DocumentStore'
}

db = MongoEngine(app)
#db.init_app(app)

# Define Users
class User(me.Document):
    userKey = me.StringField(required=True)
    firstName = me.StringField()
    lastName = me.StringField()
    workID = me.StringField()
    associatedDocuments = me.ListField()

# Define Files
class File(me.Document):
    fileID = me.StringField(required=True)
    userKey = me.StringField
    firstName = me.StringField
    lastName = me.StringField
    workID = me.StringField
    metadata = me.ListField()

# will be for GUI and uploading documents
@app.route('/document')
def foo():
    return 'Welcome to News / Document Analyzer!'

# update a user entry 
@app.route('/document/update/user')
def updateUser():
    parser = reqparse.RequestParser()
    parser.add_argument('key', type=str, required=True, help="key cannot be blank! \n")
    parser.add_argument('form', type=str, required=True, help="form cannot be blank! \n")
    parser.add_argument('data', type=str, required=True, help="data cannot be blank! \n")
    args = parser.parse_args()
    key = args['key']
    form = args['form']
    data = args['data']
    tmpUser = User.objects(userID=key)
    if tmpUser == None:
        return 'User does not exist or key is incorrect!'
    elif form == 'userKey':
        tmpUser.update_one(userKey=data)
        return 'Updated User Key! \n'
    elif form == 'firstName':
        tmpUser.update_one(firstName=data)
        return 'Updated first name! \n'
    elif form == 'lastName':
        tmpUser.update_one(lastName=data)
        return 'Updated last name! \n'
    elif form == 'workID':
        tmpUser.update_one(workID=data)
        return 'Updated Work ID! \n'
    elif form == 'associatedDocuments':
        tmpUser.update_one(associatedDocuments= tmpUser.associatedDocuments + data)
        return 'Updated associated documents list! \n'
    else:
        return 'Form does not match any fields, please change form and try again \n'

    return 'Exited without updating user \n'

# update a document entry
@app.route('/document/update/doc', methods=['PUT'])
def updateDoc():
    parser = reqparse.RequestParser()
    parser.add_argument('key', type=str, required=True, help="key cannot be blank!\n")
    parser.add_argument('file', type=str, required=True, help="file name cannot be blank!\n")
    parser.add_argument('form', type=str, required=True, help="form cannot be blank!\n")
    parser.add_argument('data', type=str, required=True, help="data cannot be blank!\n")
    args = parser.parse_args()
    key = request.form['key']
    fileID = args['file']
    form = args['form']
    data = args['data']
    tmpDoc = File.objects(fileID=fileID,userKey=key)
    if tmpDoc == None:
        return 'Could not find matching object or key was incorrect! \n'
    elif form == 'userKey':
        tmpDoc.update_one(userKey=data)
        return 'Updated User Key! \n'
    elif form == 'firstName':
        tmpDoc.update_one(firstName=data)
        return 'Updated first name! \n'
    elif form == 'lastName':
        tmpDoc.update_one(lastName=data)
        return 'Updated last name! \n'
    elif form == 'workID':
        tmpDoc.update_one(workID=data)
        return 'Updated Work ID! \n'
    elif form == 'metadata':
        tmpDoc.update_one(metadata= tmpUser.metadata + data)
        return 'Updated associated documents list! \n'
    else:
        return 'Form does not match any fields, please change form and try again \n'
    
    return 'Exited without updating document \n'

# create a User
@app.route('/document/create/user' , methods=['PUT'])
# create user
def put():
    parser = reqparse.RequestParser()
    parser.add_argument('key' , type=str, required=True, help="key cannot be blank! \n")
    parser.add_argument('first' , type=str, required=True, help="First name cannot be blank! \n")
    parser.add_argument('last' , type=str, required=True, help="last name cannot be blank! \n")
    args = parser.parse_args()
    newUser = User(userKey=args['key'], firstName=args['first'],lastName=args['last'])
    newUser.save()
    return 'Generated User! \n'

# create a document entry
@app.route('/document/create/doc' , methods=['PUT'])
# create doc
def put():
    parser = reqparse.RequestParser()
    parser.add_argument('key', type=str, required=True, help="key cannot be blank! \n")
    parser.add_argument('file', type=str, required=True, help="file name cannot be blank! \n")
    args = parser.parse_args()
    # first save the document the database
    newDoc = File(userKey=args['key'],fileID=args['file'])
    newDoc.save()
    # update users profile that matches key with associated document
    tmpUser = User.objects(userID=args['key'])
    tmpUser.update_one(associatedDocuments = tmpUser.associatedDocuments + args['file'])
    return 'Generated Document! \n'

# query from user collection
@app.route('/document/query/user', methods=['PUT'])
def readUser():
    parser.reqparse.RequestParser()
    parser.add_argument('key', type=str, required=True, help="key cannot be blank! \n")
    args = parser.parse_args()
    key = args['key']
    # find user
    tmpUser = User.objects(userKey=key)
    if tmpUser == None:
        return 'User not found ! \n'
    output = "userKey: " + tmpUser.userKey + "\n" + "firstName: " + tmpUser.firstName + "\n" + "lastName: " + tmpUser.lastName + " \n" + "workID: " + tmpUser.workID + "\n"
    output = output + "associatedDocuments: \n"
    for x in tmpUser.associatedDocuments:
        output = output + x + "\n"

    return output

# query from document collection
@app.route('/document/query/doc', methods=['PUT'])
def readDoc():
    parser.reqparse.RequestParser()
    parser.add_argument('key', type=str, required=True, help="key cannot be blank! \n")
    parser.add_argument('file', type=str, required=True, help="file name cannot be blank! \n")
    args = parser.parse_args()
    key = args['key']
    fileID = args['file']
    # find user
    tmpDoc = User.objects(fileID=fileID,userKey=key)
    if tmpDoc == None:
        return 'User not found ! \n'
        
    output = "fileID: " + tmpDoc.fileID + "\n" + "userKey: " + tmpDoc.userKey + "\n" + "firstName: " + tmpDoc.firstName + "\n" + "lastName: " + tmpDoc.lastName + " \n" + "workID: " + tmpDoc.workID + "\n"
    output = output + "metadata: \n"
    for x in tmpUser.metadata:
        output = output + x + "\n"

    return output

if __name__ == '__main__':
     app.run(debug=True)





