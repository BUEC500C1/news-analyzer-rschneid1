# Testing creating user
import SecureFileUploader as up

first = "John"
last = "Smith"
key = "Smith60"

print(up.createUser(first, last, key))

first = "Bob"
last = "Schneider"
key = "Bob60"

print(up.createUser(first,last,key))
