# Author: Ryan Schneider
# Contains the functions for secure file uploader
# Authentication is provided through specific keys that are auto-generated

import json
from requests import put,get

# Creating a user
def createUser(first, last, key):
  r = put('http://127.0.0.1:5000/document/create/user', data={'key': key ,'first': first, 'last' : last })
  output = r.content
  return output.decode("utf-8")

# Create a document
def createDoc(key, file):
  r = put("http://127.0.0.1:5000/document/create/doc", data={'key': key, 'file': file})  
  output = r.content
  return output.decode("utf-8")

# update user
def updateUser(key, form, data):
  r = put("http://127.0.0.1:5000/document/update/user", data={'key': key ,'form': form, 'data' : data })
  output = r.content
  return output.decode("utf-8")

# update document
def updateDoc(key, file, form, data):
  r = put("http://127.0.0.1:5000/document/update/doc", data={'key': key ,'file': file, 'form' : form, 'data': data })
  output = r.content
  return output.decode("utf-8")

# query from user collection
def readUser(key):
  r = put("http://127.0.0.1:5000/document/query/user", data={'key': key })
  output = r.content
  return output.decode("utf-8")

# query from document collection
def readDoc(key, file):
  r = put("http://127.0.0.1:5000/document/query/doc", data={'key': key ,'file': file})
  output = r.content
  return output.decode("utf-8")
