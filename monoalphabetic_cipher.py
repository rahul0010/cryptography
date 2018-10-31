import random
import string
alphabets = list(string.ascii_letters)
encrypted_alphabets = random.sample(alphabets, len(alphabets))
print(alphabets)
print(encrypted_alphabets)

def encrypt(text):
    result = ""
    for i in text:
        result += encrypted_alphabets[alphabets.index(i)]
    return result

def decrypt(text):
    result = ""
    for i in text:
        result += alphabets[encrypted_alphabets.index(i)]
    return result

encrypted_text = encrypt("HelloWorld")
print("Encrypted text: ", encrypted_text)
print("Decrypted text: ",decrypt(encrypted_text))