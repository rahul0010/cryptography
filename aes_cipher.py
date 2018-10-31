from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
data = "HelloWorld"
data = data.encode("utf8")
cipher_text, tag = cipher.encrypt_and_digest(data)
print(cipher_text)
print(tag)
cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
decripted_text = cipher.decrypt_and_verify(cipher_text, tag)
print(decripted_text)