import ObjectOriented as obj

def count_letters(message):
    message = message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counts = []
    for i in range(len(alphabet)):
        counts.append(0)
    for i in range(len(message)):
        index = alphabet.find(message[i])
        if index != -1:
            counts[index] += 1
    return counts

def max_index(freq):
    max = 0
    for i in range(len(freq)):  
        if freq[i] > freq[max]:
            max = i
    return max

def split(message):
    splitted = ['', '']
    for i in range(len(message)):
        if i % 2 == 0:
            splitted[0] += message[i]
        else:
            splitted[1] += message[i]
    return splitted

def decrypt(encrypted):
    cc = obj.CaesarCypher()
    answer = ""
    splitted = split(encrypted)
    print(splitted)
    keys = [0, 0]
    for i in range(len(splitted)):
        freq = count_letters(splitted[i])
        keys[i] = max_index(freq) - 4
        if keys[i] > 26:
            keys[i] = keys[i] % 26
        elif keys[i] < 4:
            keys[i] = 22 + max_index(freq)

    first = cc.encrypt(splitted[0], 26 - keys[0])
    second = cc.encrypt(splitted[1], 26 - keys[1])
    for j in range(len(first)):
        if j < len(second):
            answer += first[j] + second[j]
        else:
            answer += first[j]
    return answer

decrypt("Akag tjw Xibhr awoa aoee xakex znxag xwko")
