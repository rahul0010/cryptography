from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
key = DES3.adjust_key_parity(get_random_bytes(24))
cipher = DES3.new(key, DES3.MODE_EAX)
text = "Helloworld".encode("utf8")
cipher_text = cipher.encrypt(text)
print(cipher_text)
cipher = DES3.new(key, DES3.MODE_EAX, cipher.nonce)
print(cipher.decrypt(cipher_text))