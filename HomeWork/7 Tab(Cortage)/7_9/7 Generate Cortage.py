def func_tpl(string, tpl_1):
    tpl = list(tpl_1)
    main_tpl = ((sym,num) for sym in string for i,num in enumerate(tpl) if string.index(sym) == i)
    return main_tpl
text = 'abc'
tpl_n = (10,20,30,40)

print(i for i in enumerate(func_tpl(text,tpl_n)))
for j in func_tpl(text,tpl_n):
    print(j)