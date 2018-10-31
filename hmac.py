from Crypto.Hash import HMAC, SHA256
secret = b'hell'
hash = HMAC.new(secret, digestmod=SHA256)
hash.update("HEllowWord".encode("utf8"))
print(hash.hexdigest())