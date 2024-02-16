def histogram(string,count=0):
    sym_dict = dict()
    for sym in string.lower():
        if sym.isalnum():
            count += 1
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1
    for sym,value in sym_dict.items():
        sym_dict[sym] = round((value / count),3)
    sym_dict_1 = dict(sorted(sym_dict.items()))
    sorted_dict = dict(sorted(sym_dict_1.items(),key=lambda item: item[1],reverse=True))
    return sorted_dict


massage = open('text.txt','r')
text = massage.read()
hist = histogram(text)
massage.close()
analysis = open('analysis.txt','w')
for sym,data in hist.items():
    analysis.write(sym)
    analysis.write(': ')
    analysis.write(str(data))
    analysis.write('\n')
analysis.close()


