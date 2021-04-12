# Test uploading a document

import NewsFeedIngester as up

key = "Bob60"
file_path = "./graphsforHW9.pdf"

print(up.ingest(key, file_path))