def start(func):
    print('</----------|>')
    return func


@start
def sandwich(*args: str):
    for i in args:
        print('  ', i)
    print('<|_________/>')


sandwich('Помидоры', 'Сыр', 'Ветчина')
