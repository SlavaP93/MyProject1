alphabet = 'abcdefg'

text_1 = alphabet[:]
text_2 = alphabet[::- 1]
text_3 = alphabet[::2]
text_4 = alphabet[1::2]
text_5 = alphabet[:1]
text_6 = alphabet[:-2:-1]
text_7 = alphabet[2:3]
text_8 = alphabet[-3::]
text_9 = alphabet[-4:-2]
text_10 = alphabet[-3:2:-1]

print(text_1)
print(text_2)
print(text_3)
print(text_4)
print(text_5)
print(text_6)
print(text_7)
print(text_8)
print(text_9)
print(text_10)