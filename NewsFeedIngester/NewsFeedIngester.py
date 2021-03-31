# Author: Ryan Schneider
# functions for the news feed ingestor
# supported file types are provided by NLP, else we can just ingest any file

# SUPPORTED FILE TYPES: PDF, .doc, .docx, .txt, JPEG, MP4 
import json
import requests *
import os


def ingest(key, file_path, filename):
  files = {
    'key': key,
    'filename': filename,
    'file': open(file_path, 'rb')
  }
  r = requests.post('https://localhost/document/upload', files=files)
  return key

