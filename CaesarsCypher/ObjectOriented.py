class CaesarCypher():    
    
    def __init__(self, message, key)
        self._message = message
        self._key = key

    def shift(string, key):
    return string[key:] + string[:key]

    def encrypt(message, key1, key2):
    result = ""
    message = message.lower()
    shifted1 = shift(alphabet, key1)
    shifted2 = shift(alphabet, key2)
    for i in range(len(message)):
        index = alphabet.find(message[i])
        result += shifted1[index] if i % 2 == 0 else shifted2[index]
    return result