def funs_sqrt(data):
    answer = []
    for i_data in data:
        try:
            if not isinstance(i_data,(int)):
                raise TypeError('Ошибка значения!')
            if i_data < 1:
                raise ValueError('Отрицательное число или 0')
            else:
                answer.append(i_data^2)
        except (ValueError,TypeError) as log_error:
            answer.append(log_error)
            continue

    return answer


spis = [1,4,6,-1,0,'a',23.2]
print(funs_sqrt(spis))