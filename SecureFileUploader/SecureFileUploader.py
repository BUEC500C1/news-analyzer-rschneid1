# Author: Ryan Schneider
# Contains the functions for secure file uploader
# Authentication is provided through specific keys that are auto-generated

import json
from requests import put,get

# Creating a user
def createUser(first, last, key):
  put('http://127.0.0.1:5000/document/create/user', data={'key': key ,'first': first, 'last' : last })
  return key

# Create a document
def createDoc(key, file):
  put("http://127.0.0.1:5000/document/create/doc", data={'key': key, 'file': file})  
  return key

# update user
def updateUser(key, form, data):
  put("http://127.0.0.1:5000/document/update/user", data={'key': key ,'form': form, 'last' : data })
  return key

# update document
def updateDoc(key, file, form, data):
  put("http://127.0.0.1:5000/document/update/doc", data={'key': key ,'file': file, 'form' : form, 'data': data })
  return key

# query from user collection
def readUser(key):
  put("http://127.0.0.1:5000/document/query/user", data={'key': key })
  return "Returned Result ! \n"

# query from document collection
def readDoc(key, file):
  put("http://127.0.0.1:5000/document/query/doc", data={'key': key ,'file': first})
  return "Returned Result ! \n"
