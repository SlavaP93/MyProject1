stroka = input('Message: ')
sym = input('Symbol: ')
message = [i * 2 for i in stroka]
print(message)
message_2 = [i * 2 + sym for i in stroka]
print(message_2)