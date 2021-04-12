# test for updating user

import SecureFileUploader as up

key = "Smith60"
newKey = "Fax60"
first = "Kyle"
last = "Johnson"
workID = "City Department"
document1 = "Memo1"

# update key
data = newKey
form = "userKey"
print(up.updateUser(key,form,data))
# update first
data = first
form = "firstName"
print(up.updateUser(newKey,form,data))
# update last
data = last
form = "lastName"
print(up.updateUser(newKey,form,data))
# update workID
data = workID
form = "workID"
print(up.updateUser(newKey,form,data))
# update documents
data = document1
form = "associatedDocuments"
print(up.updateUser(newKey,form,data))