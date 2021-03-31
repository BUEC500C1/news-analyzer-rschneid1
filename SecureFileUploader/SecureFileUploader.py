# Author: Ryan Schneider
# Contains the functions for secure file uploader
# Authentication is provided through specific keys that are auto-generated

import json
from requests import put,get

# Creating a user
def createUser(first, last, key):
  put(http://localhost/document/create/user, data={'key': key ,'first': first, 'last' : last }).json()
  return key

# Create a document
def createDoc(key, file):
  put(http://localhost/document/create/doc), data={'key': key, 'file': file}).json()  
  return key

# update user
def updateUser(key, form, data):
  put(http://localhost/document/update/user, data={'key': key ,'form': form, 'last' : data }).json()
  return key

# update document
def updateDoc(key, file, form, data):
  put(http://localhost/document/update/doc, data={'key': key ,'file': file, 'form' : form, 'data': data }).json()
  return key

# query from user collection
def readUser(key):
  put(http://localhost/document/query/user, data={'key': key }).json()
  return "Returned Result ! \n"

# query from document collection
def readDoc(key, file):
  put(http://localhost/document/query/doc, data={'key': key ,'file': first}).json()
  return "Returned Result ! \n"

  
