# Test script for updating documents

import SecureFileUploader as up

key = "Bob60"
fileID = "Memo1"
authorFirst = "Kelly"
authorLast = "Washington"
workID = "Author"
metadata = "Date Written: 1928"

# update fileID
form = "fileID"
data = fileID
print(up.updateDoc(key, fileID, form, data))

# update author first
form = "firstName"
data = authorFirst
print(up.updateDoc(key, fileID, form, data))

# update author last
form = "lastName"
data = authorLast
print(up.updateDoc(key, fileID, form, data))

# update date workID
form = "workID"
data = workID
print(up.updateDoc(key, fileID, form, data))

# update metadata
form = "metadata"
data = metadata
print(up.updateDoc(key, fileID, form, data))
