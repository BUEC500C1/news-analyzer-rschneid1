# Author: Ryan Schneider
# functions for the news feed ingestor
# supported file types are provided by NLP, else we can just ingest any file

# SUPPORTED FILE TYPES: PDF, .doc, .docx, .txt, JPEG, MP4 
import json
import requests
import os


def ingest(key, file_path):
  files = {'file': open(file_path, 'rb') }
  meta = {
    'key': key
  }
  r = requests.post('http://127.0.0.1:5000/document/upload', files=files, data=meta)
  return r.content
