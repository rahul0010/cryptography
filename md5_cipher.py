from Crypto.Hash import MD5
text = "Hello world".encode("utf8")
hash = MD5.new()
hash.update(text)
print(hash.hexdigest())