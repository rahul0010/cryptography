def encrypt(text,key):
    ptr = 0
    result = ""
    for i in text:
        result += chr(ord(i) ^ ord(key[ptr]))
        if(ptr == len(key)-1):
            ptr = 0
    return result

encrypted_text = encrypt("helloworlditgoodday","justrandom")
print("Encrypted Text: ",encrypted_text)
print("Decrypted Text: ",encrypt(encrypted_text,"justrandom"))
