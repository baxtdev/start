def null_decorator(func):
    print(func.__name__)
    return func

@null_decorator
def greet():
    return 'Hello!'

greet = null_decorator(greet)

print(greet())