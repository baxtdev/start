"""Создайте функцию average_calculator, которая будет возвращать другую функцию. 
Внутренняя функция должна принимать числа и возвращать их среднее арифметическое. 
Пример использования:"""

def average_calculator():
    a=0
    x=0
    def counter(args):
        nonlocal a
        nonlocal x
        a+=args
        x+=1
        return a/x
     
    return counter    

# a=average_calculator()
# print(a(10))
# print(a(20))
# print(a(30))  

import time
"""
Напишите декоратор @retry,
 который будет повторять выполнение функции, если она вызвала исключение. 
Декоратор должен принимать максимальное количество попыток и интервал между ними. 
Пример использования
"""
def retry(max_attemps,interval):
    def retry_decorator(func):
        def wrapper(args,arg):
            attemps=0
            while attemps<max_attemps:
                try:
                    return func(args,arg)
                
                except Exception as e:
                    print(f"Exception occurred: {e}. Retrying in {interval} seconds...")
                    time.sleep(interval)
                    attemps += 1
            print(f"Max attempts reached. Function {func.__name__} failed.")
        return wrapper    
    return retry_decorator


@retry(max_attemps=3,interval=2)
def some_function(x,y):
    print(x/0)
    return "sucses"

some_function(2,9)