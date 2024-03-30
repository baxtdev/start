def outer():  # внешняя функция
    n = 5
 
    def inner():    # вложенная функция
        n = 25
        print(n)
 
    inner()     # 25
    print(n)
 
 
outer()     # 5 
# 25    - inner
# 5     - outer

def outer():  # внешняя функция
    n = 5
 
    def inner():    # вложенная функция
        nonlocal n  # указываем, что n - это переменная из окружающей функции
        n = 25
        print(n)
 
    inner()     # 25
    print(n)
 
 
outer()          # 25