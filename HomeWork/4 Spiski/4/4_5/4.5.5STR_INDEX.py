maessage = ['hqwehrty']
sym_start = maessage[0].index('h')
sym_end = maessage[0].rindex('h')
new_message = maessage[0][sym_end - 1:sym_start:-1]
print(new_message)