text = ('Я! есть, Грут?')
symb = set(".,;:!?")
count = 0
for i_sym in text:
    if i_sym in symb:
        count += 1

print(count)