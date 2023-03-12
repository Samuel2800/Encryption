class CaesarCypher():    
    
    def __init__(self):
        self

    def shift(self, string, key):
        return string[key:] + string[:key]

    def encrypt(self, message, key):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        result = ""
        message = message.lower()
        shifted = self.shift(alphabet, key)
        for i in range(len(message)):
            if message[i] == " ":
                result += " "
            else:
                index = alphabet.find(message[i])
                result += shifted[index]
        return result