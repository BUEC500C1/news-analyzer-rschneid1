# Test PDF Mining
# For Ingester
# Author: Ryan Schneider
# References:

import PyPDF2 as pypdf

# *** TEST ***
#pdfObject = open('name.pdf','rb')
#pdf = pypdf.PdfFileReader(pdfobject)
#print(pdfReader.numPages)
## create a page object
#pageObj = pdfReader.getPage(0)
## extract text from page
#print(pageObj.extractText())
## closing the pdf file object
#pdfFileObj.close()
# *** END TEST ***

# function for navigating xml
def findInDict(needle, haystack):
    for key in haystack.keys():
        try:
            value = haystack[key]
        except:
            continue
        if key == needle:
            return value
        if isinstance(value,dict):
            x = findInDict(needle,value)
            if x is not None:
                return x

# *** READ XML ***
pdfobject = open('CTRX_filled.pdf','rb')

pdf = pypdf.PdfFileReader(pdfobject)

xfa = findInDict('/XFA', pdf.resolveObjects)
xml = xfa[7].getObject().getData()

# *** PARSING ***
# Data forms:
# fileID
# metadata:
# author
