# Author: Ryan Schneider
# functions for the news feed ingestor

# SUPPORTED FILE TYPES: PDF, .doc, .docx, 
import json

def ingestPDF(file):
  # read PDF and detect metadata to fill out JSON object
  jsonObj = file
  return jsonObj

def ingestMSDOC(file):
  # read DOC/DOCX and detect metadata to fill out JSON object
  jsonObj = file
  return jsonObj

def ingestTXT(file):
  # read .txt and detect metadata to fill out JSON object
  jsonObj = file
  return jsonObj

def ingestJPEG(file, fields):
  # read JPEG and detect metadata to fill out JSON object
  return 1

def ingestMP4(file, fields):
  # read MP4 and detect metadata to fill out JSON object
  return 1
# Provides fields for user to fill out their own metadata
def ingestCustom(fields):
  return 1
# User enters data and desired fields and it creates object, or can use standard fields
def createFields():
  return 1
  

