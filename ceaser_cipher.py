def enrypt(text, key):
    text = text.upper()
    result = ""
    for i in text:
        result += chr(((ord(i) + key) % 26) + ord('A'))
    return result

def decrypt(text, key):
    text = text.upper()
    result = ""
    for i in text:
        result += chr(((ord(i) - key) % 26) + ord('A'))
    return result

encrypted_text = enrypt("HelloWorld", 3)
print("Encrypted Text: ",encrypted_text)
print("Decrypted Text: ",decrypt(encrypted_text, 3))