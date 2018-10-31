from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
key = get_random_bytes(8)   
cipher = DES.new(key, DES.MODE_EAX)
text = "Hello world"
text = text.encode("utf8")
cipher_text = cipher.encrypt(text)
print(cipher_text)
cipher = DES.new(key, DES.MODE_EAX, cipher.nonce)
print(cipher.decrypt(cipher_text))