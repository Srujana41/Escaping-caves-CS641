#  import numpy as np
ciphertext="qmnjvsanvwewcflctvprjtjtvvplvlfvxjavqildhcxmlnvcnacyclpafcgytvfvwfvwgqyppqqpqcsywsqrxqmnjvafycgvtlvhfcwtylaeuqfvxjatkbvcqnsqslhfavawnccveasfuqbqvqtcyllrqrxxwacfypsdcuqfavrqcgefqpyattracxwvtaawwddveasflcbqvdtrawmvupqquwxdecgqcwtyqyaflvlqsyqklhqsnafqvmllhvqpawrnqgvfusrecwawyqpfnwgawdgf"
altered_cipher = ciphertext
print("The cipher without any special characters is ")
print(altered_cipher)

print("The length of the cipher is "+str(len(altered_cipher)))

mapping = {
        'a': 't',
        'b': 'v',
        'c': 'i',
        'd': 'u',
        'e': 'c',
        'f': 'h',
        'g': 'g',
        'h': 'p',
        'i': 'q',
        'j': 'b',
        'k': '?',
        'l': 's',
        'm': 'k',
        'n': 'r',
        'o': '?',
        'p': 'd',
        'q': 'a',
        'r': 'w',
        's': 'f',
        't': 'l',
        'u': 'm',
        'v': 'e',
        'w': 'o',
        'x': 'y',
        'y': 'n',
        'z': '?'
        }

temp = ""
for ch in altered_cipher.lower():
    temp += mapping[ch]

print(temp)

plaintext = ""
for i in range(int(len(temp)/5)):
    plaintext+=temp[i*5+3]
    plaintext+=temp[i*5+2]
    plaintext+=temp[i*5+4]
    plaintext+=temp[i*5]
    plaintext+=temp[i*5+1]
    

print("The plain text is")
print(plaintext+ temp[280:284])

