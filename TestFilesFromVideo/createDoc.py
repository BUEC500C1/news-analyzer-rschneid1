# Test script for creating a document

import SecureFileUploader as up

key = "Smith60"
fileID = "Test Document"

print(up.createDoc(key, fileID))

key = "Bob60"
fileID = "Memo1"
print(up.createDoc(key, fileID))
fileID = "Memo2"
print(up.createDoc(key, fileID))
