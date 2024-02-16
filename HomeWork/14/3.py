
def decor(func):
    def do_twice(*args):
        do_twice.count += 1
        print(do_twice.count)
        return func(*args)
    do_twice.count = 0
    return do_twice


@decor
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('tom')
greeting('Ivan')
greeting('sasha')