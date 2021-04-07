# Author: Ryan Schneider
# Natural Language Processing
# Provide functions to interact with documents and text

import PyPDF2 as pd

# extracts text and outputs it to command line
def extractText(file_path):
    pdfFileObj = open(file_path, 'rb')
    
    pdfReader = pd.PdfFileReader(pdfFileObj)

    numPages = pdfReader.numPages

    pageObj = pdfReader.getPage(0)

    output = pageObj.extractText()

    for i in range(1,numPages):
        pageObj = pdfReader.getPage(i)
        temp = pageObj.extractText()
        output = output + temp

    pdfFileObj.close()

    return output
