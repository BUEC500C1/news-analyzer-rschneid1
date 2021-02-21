from NewsFeedIngester import *

# test various functions
def test_ingestPDF():
  file = "www.google.com/user/schneid/pdf1"
  assert ingestPDF(file) == file

def test_ingestMSDOC():
  file = "www.google.com/user/schneid/file.doc"
  assert ingestMSDOC(file) == file

def test_ingestTXT():
  file = "www.google.com/user/schneid/file.txt"
  assert ingestTXT(file) == file

def test_ingestJPEG():
  file = "www.google.com/user/schneid/file.jpeg"
  fields = "author: Ryan Schneider"
  assert ingestJPEG(file, fields) == 1

def test_ingestMP4(file, fields):
  file = "www.google.com/user/schneid/file.jpeg"
  fields = "author: Ryan Schneider"
  assert ingestMP4file, fields) == 1
  
  
def test_ingestCustom(fields):
  fields = "author: Ryan Schneider"
  assert ingestCustom(fields) == 1
  
def test_createFields():
  assert createFields() == 1
