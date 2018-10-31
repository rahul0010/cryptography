def encrypt(layers, text):
    rail = [""]*layers
    layer = 0
    for i in plain_text:
        rail[layer] += i
        if(layer >= layers-1):
            layer = 0
        else:
            layer += 1
    cipher = "".join(rail)
    return cipher

layers = 3
plain_text = "HelloWorld"
cipher_text = encrypt(layers, plain_text)
print(cipher_text)