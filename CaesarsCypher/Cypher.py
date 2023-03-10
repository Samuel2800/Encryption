alphabet = "abcdefghijklmnopqrstuvwxyz" 

def shift(string, key):
    return string[key:] + string[:key]

def encrypt(message, key):
    result = ""
    message = message.lower()
    shifted = shift(alphabet, key)
    for i in range(len(message)):
        index = alphabet.find(message[i])
        result += shifted[index]
    return result
