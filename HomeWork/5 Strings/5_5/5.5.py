while True:
    password = input('Придумайте пароль: ')
    sum = 0
    numer = [sum + 1 for digit in password if digit.isdigit()]
    if len(password) < 8 or password.islower() or password.isalpha() or not password.isascii() or len(numer) < 3:
        print('Слабый пароль, попробуйте придумать получше!')
    else:
        print('Отличный пароль!')
        break