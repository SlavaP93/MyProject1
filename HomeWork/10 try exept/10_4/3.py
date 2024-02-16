with open('reg_file.txt','r',encoding='utf-8') as regdata:
    lstdata = [i_line.split(' ') for i_line in regdata]
    with open('good.log','w',encoding='utf-8') as good_reg:
        with open('bad_reg.log','a',encoding='utf-8') as bad_reg:
            for i_data in lstdata:
                try:
                    if len(i_data) < 3:
                        bad_reg.write(' '.join(i_data))
                        raise IndexError('    Не хватает элемента')
                    i_data[2] = i_data[2].removesuffix('\n')
                    if not i_data[0].isalpha():
                        bad_reg.write(' '.join(i_data))
                        raise NameError('    В имени могут быть только буквы!')
                    if '@' not in i_data[1] or '.' not in i_data[1]:
                        bad_reg.write(' '.join(i_data))
                        raise SyntaxError('      Не правильный емейл')
                    if int(i_data[2]) < 10 or int(i_data[2]) > 99:
                        bad_reg.write(' '.join(i_data))
                        raise ValueError('     Несоответствующий условию возраст')
                    else:
                        good_reg.write(' '.join(i_data))
                        good_reg.write('\n')
                except (IndexError,NameError,SyntaxError,ValueError) as file:
                    bad_reg.write(str(file))
                    bad_reg.write('\n')
                    continue
