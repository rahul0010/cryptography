def encrypt(string, shift):
    result = ""
    for i in string:
        if(i.isupper()):
            result += chr((ord(i) + shift))
        else:
            result += chr((ord(i) + shift))
    return result
encrypted=encrypt("Hello World",4)
print(encrypted)

def decrypt(string, shift):
    result = ""
    for i in string:
        if(i.isupper()):
            result += chr((ord(i) - shift))
        else:
            result += chr((ord(i) - shift))
    return result

print(decrypt(encrypted,4))