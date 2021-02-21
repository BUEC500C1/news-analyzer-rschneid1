from SecureFileUploader import *

def test_userGen():
  account = "Ryan Schneider"
  key = 1
  assert userGen(account,key) == key
  
def test_create():
  account = "Ryan Schneider"
  key = 1
  tree = "/users/ryanSchneid/PDFfield"
  assert create(tree, account, key) == 1

def test_update():
  arrayOfTrees = ["users", "ryan"]
  fields = "pdf"
  account = "Ryan Schneider"
  key = 1
  assert update(arrayOfTrees, fields, account, key) == 1

def read():
  tree = "/users/ryanSchneid/PDFfield"
  fields = "pdf"
  amount = 8
  account = "Ryan Schneider"
  key = 1
  assert read(tree, fields, amount, account, key)

