def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция '{func.__name__}' была вызвана {count} раз.")
        return func(*args, **kwargs)
    return wrapper

@counter
def say_hello(name):
    return f"Hello, {name}!"

say_hello("John")
say_hello("John")
say_hello("John")

def counter(func):
    def wrapper(*args, **kwargs):
        count = 0
        print(f"Function '{func.__name__}' called {count + 1} times.")
        result = func(*args, **kwargs)
        count += 1
        return result
    return wrapper

@counter
def say_hello(name):
    return f"Hello, {name}!"

say_hello("John")
say_hello("John")
say_hello("John")