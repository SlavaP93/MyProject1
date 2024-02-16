text = 'so~mec~od~e'
sym_count = []

for index, sym in enumerate(text):
    if sym == '~':
        sym_count.append(str(index))

print(' '.join(sym_count))