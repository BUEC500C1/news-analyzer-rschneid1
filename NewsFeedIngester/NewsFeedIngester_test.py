from NewsFeedIngester import *

# test various functions
def test_ingestPDF():
  file = "www.google.com/user/schneid/pdf1"
  assert ingestPDF(file) == file

def test_ingestMSDOC():
  file = "www.google.com/user/schneid/file.doc"
  assert ingestMSDOC(file) == file
