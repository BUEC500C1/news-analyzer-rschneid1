# Local Flask Application
# Designed to be deployed on AWS
# Author: Ryan Schneider
# References: https://flask.palletprojects.com


# flask
from flask import Flask, request, flash, redirect, url_for
from flask_restful import Resource, Api, reqparse


# file ingester
import os
from werkzeug.utils import secure_filename

UPLOAD_BASE_PATH = './data/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
api = Api(app)

# Using PyMongo
from pymongo import MongoClient
import json
client = MongoClient('localhost',27017)
db = client['DocumentStore']
# set up collection
userCollection = db['users']
docCollection = db['docs']


# Using MongoEngine
#from flask_mongoengine import MongoEngine
#import mongoengine as me
#app.config['MONGODB_SETTINGS'] = {
#    'db': 'DocumentStore'
#}
#db = MongoEngine()
#db.init_app(app)

#class User(db.Document):
#    userKey = db.StringField(required=True)
#    firstName = db.StringField()
#    lastName = db.StringField()
#    workID = db.StringField()
#    associatedDocuments = db.ListField()

#class File(db.Document):
#    fileID = db.StringField(required=True)
#    userKey = db.StringField
#    firstName = db.StringField
#    lastName = db.StringField
#    workID = db.StringField
#    metadata = db.ListField()


# Define Users
User = {
    "_id": "",
    "userKey": "",
    "firstName": "",
    "lastName": "",
    "workID": "",
    "associatedDocuments": []
}

# Define Files
Document = {
    "_id": "",
    "fileID": "",
    "userKey": "",
    "firstName": "",
    "lastName": "",
    "workID": "",
    "metadata": []
}

# *** DEFINE HELPER FUNCTIONS **

# check if supported file type
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# *** END HELPER FUNCTIONS ***


# Welcome URI
@app.route('/document')
def foo():
    return 'Welcome to News / Document Analyzer!'

# File Ingester
@app.route('/document/upload' , methods=['POST'])
def file_ingester():
    if request.method == 'POST':
        # check if user key exists in request
        if 'key' not in request.form:
            return "Could not ingest document: No Key Provided"
        # check if user directory exists:
        USER_PATH = UPLOAD_BASE_PATH + request.form['key']
        isFile = os.path.isfile(USER_PATH)
        if(isFile==None):
            return "Could not ingest Document: User does not exist" 
        # check if file exists in request
        if 'file' not in request.files:
            return "Could not ingest Document: file was not included with upload"
        file = request.files['file']
        # also check if filename is blank
        if file.filename == '':
            return "Could not ingest Document: Filename is blank!"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(USER_PATH, filename))
            return "File Successfully uploaded!"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# update a user entry 
@app.route('/document/update/user', methods=['PUT'])
def updateUser():
    parser = reqparse.RequestParser()
    parser.add_argument('key', type=str, required=True, help="key cannot be blank! \n")
    parser.add_argument('form', type=str, required=True, help="form cannot be blank! \n")
    parser.add_argument('data', type=str, required=True, help="data cannot be blank! \n")
    args = parser.parse_args()
    key = args['key']
    form = args['form']
    data = args['data']
    tmpUser = userCollection.find_one({"userKey": key})
    if tmpUser == None:
        return 'User does not exist or key is incorrect!'
    elif form == 'userKey':
        newQuery = { "userKey": key} 
        newValues = {"$set" : {"userKey": data} }
        userCollection.update_one(newQuery, newValues)
        return 'Updated User Key! \n'
    elif form == 'firstName':
        newQuery = { "userKey": key}  
        newValues = {"$set" : {"firstName": data} }
        userCollection.update_one(newQuery, newValues)
        return 'Updated first name! \n'
    elif form == 'lastName':
        newQuery = { "userKey": key}  
        newValues = {"$set" : {"lastName": data} }
        userCollection.update_one(newQuery, newValues)
        return 'Updated last name! \n'
    elif form == 'workID':
        newQuery = { "userKey": key}  
        newValues = {"$set" : {"workID": data} }
        userCollection.update_one(newQuery, newValues)
        return 'Updated Work ID! \n'
    elif form == 'associatedDocuments':
        # check if document update exists
        tmpDoc = docCollection.find_one({"fileID": data})
        if tmpDoc == None:
            return "Document does not exist ! \n"
        newQuery = { "userKey": key}
        tmpUser['associatedDocuments'].append(data)  
        newValues = {"$set" : {"associatedDocuments": tmpUser['associatedDocuments']} }
        userCollection.update_one(newQuery, newValues)
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
    # check if key and fileID combination exist:
    tmpDoc = docCollection.find_one({"userKey": key, "fileID": fileID})
    if tmpDoc == None:
        return 'Could not find matching object or key was incorrect! \n'
    elif form == 'userKey':
        newQuery = { "userKey": key, "fileID": fileID} 
        newValues = {"$set" : {"userKey": data} }
        docCollection.update_one(newQuery, newValues)
        return 'Updated User Key! \n'
    elif form == 'firstName':
        newQuery = { "userKey": key, "fileID": fileID}  
        newValues = {"$set" : {"firstName": data} }
        docCollection.update_one(newQuery, newValues)
        return 'Updated first name! \n'
    elif form == 'lastName':
        newQuery = { "userKey": key, "fileID": fileID}  
        newValues = {"$set" : {"lastName": data} }
        docCollection.update_one(newQuery, newValues)
    elif form == 'workID':
        newQuery = { "userKey": key, "fileID": fileID}  
        newValues = {"$set" : {"workID": data} }
        docCollection.update_one(newQuery, newValues)
        return 'Updated Work ID! \n'
    elif form == 'metadata':
        newQuery = { "userKey": key, "fileID": fileID}
        tmpDoc['metadata'].append(data)  
        newValues = {"$set" : {"metadata": tmpDoc['metadata'] } }
        docCollection.update_one(newQuery, newValues)
        return 'Updated associated documents list! \n'
    else:
        return 'Form does not match any fields, please change form and try again \n'
    
    return 'Exited without updating document \n'

# create a User
@app.route('/document/create/user' , methods=['PUT'])
# create user
def createUser():
    parser = reqparse.RequestParser()
    parser.add_argument('key' , type=str, required=True, help="key cannot be blank! \n")
    parser.add_argument('first' , type=str, required=True, help="First name cannot be blank! \n")
    parser.add_argument('last' , type=str, required=True, help="last name cannot be blank! \n")
    args = parser.parse_args()
    #check if folder exists
    #if folder exists generate error
    #if folder does not exist create folder and generate user
    USER_PATH = UPLOAD_BASE_PATH + args['key']
    print(args['key'])
    tmpUser = userCollection.find_one({"userKey": args['key']})

    if tmpUser == None:
        # create user path and upload object for mongo db
        newUser = User
        tmpVar = newUser['_id'] + args['first'] + args['key']
        newUser['_id'] = tmpVar
        newUser['userKey'] = args['key']
        newUser['firstName'] = args['first']
        newUser['lastName'] = args['last']
        post_id = userCollection.insert_one(newUser).inserted_id
        print(post_id)
        os.mkdir(USER_PATH)
        return 'Generated User!'
    else:
        return "Database Error: User already exists!"

# create a document entry
@app.route('/document/create/doc' , methods=['PUT'])
# create doc
def createDoc():
    parser = reqparse.RequestParser()
    parser.add_argument('key', type=str, required=True, help="key cannot be blank! \n")
    parser.add_argument('file', type=str, required=True, help="file name cannot be blank! \n")
    args = parser.parse_args()
    # Check if User exists (who is trying to create a document)
    USER_PATH = UPLOAD_BASE_PATH + args['key']
    tmpUser = userCollection.find_one({"userKey": args['key']})
    if tmpUser == None:
        return 'User does not exist!'
    # check if document already exists
    tmpDoc = docCollection.find_one({"fileID": args['file']})
    if tmpDoc == None:
        # save the document the database
        newDoc = Document
        tmpVar = newDoc['_id'] + args['key'] + args['file']
        newDoc['_id'] = tmpVar
        newDoc['userKey'] = args['key']
        newDoc['fileID'] = args['file']
        post_id = docCollection.insert_one(newDoc).inserted_id
        # update users profile that matches key with associated document
        #tmpUser = userCollection.find_one({"userKey": args['key']})
        tmpUser['associatedDocuments'].append(args['file'])
        newQuery = {"userKey": args['key']}
        newValues = {"$set" : {"associatedDocuments": tmpUser['associatedDocuments']} }
        userCollection.update_one(newQuery, newValues)
        return 'Generated Document and Linked to User !'
    else:
        return 'File ID already exists ! '
        

# query from user collection
@app.route('/document/query/user', methods=['PUT'])
def readUser():
    parser = reqparse.RequestParser()
    parser.add_argument('key', type=str, required=True, help="key cannot be blank! \n")
    args = parser.parse_args()
    key = args['key']
    # find user
    tmpUser = userCollection.find_one({"userKey": key})
    if tmpUser == None:
        return 'User not found ! \n'
    output = "userKey: " + tmpUser['userKey'] + "\n" + "firstName: " + tmpUser['firstName'] + "\n" + "lastName: " + tmpUser['lastName'] + " \n" + "workID: " + tmpUser['workID'] + "\n"
    output = output + "associatedDocuments: \n"
    for x in tmpUser['associatedDocuments']:
        output = output + x + "\n"

    return output

# query from document collection
@app.route('/document/query/doc', methods=['PUT'])
def readDoc():
    parser = reqparse.RequestParser()
    parser.add_argument('key', type=str, required=True, help="key cannot be blank! \n")
    parser.add_argument('file', type=str, required=True, help="file name cannot be blank! \n")
    args = parser.parse_args()
    key = args['key']
    fileID = args['file']
    # check for key and fileID combination
    tmpDoc = docCollection.find_one({"userKey": key,"fileID": fileID})
    if tmpDoc == None:
        return 'Document not found with that key and document combination!'
    else:
        # read document
        output = "fileID: " + tmpDoc['fileID'] + "\n" + "userKey: " + tmpDoc['userKey']+ "\n" + "firstName: " + tmpDoc['firstName'] + "\n" + "lastName: " + tmpDoc['lastName'] + " \n" + "workID: " + tmpDoc['workID'] + "\n"
        output = output + "metadata: \n"
        for x in tmpDoc['metadata']:
            output = output + x + "\n"
        return output

if __name__ == '__main__':
     app.run(debug=True)



