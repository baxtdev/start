"""
Определение функции начинается с выражения def, 
которое состоит из имени функции, набора скобок с параметрами и двоеточия. 
Параметры в скобках необязательны.
 А со следующей строки идет блок инструкций, которые выполняет функция. 
 Все инструкции функции имеют отступы от начала строки.
"""

def say_hello():
    print("Hello")


def say_hello():    # определение функции say_hello
    print("Hello")
 

def say_hello(): print("Hello")
 

def main():
    say_hello()
    say_goodbye()
 
def say_hello():
    print("Hello")
 
def say_goodbye():
    print("Good Bye")
 
# Вызов функции main
main()

def say_hello(): print("Hello")
def say_goodbye(): print("Good Bye")
 
message = say_hello
message()       # Hello
message = say_goodbye
message()       # Good Bye


def sum(a, b): return a + b
def multiply(a, b): return a * b
 
operation = sum
result = operation(5, 6)
print(result)   # 11
 
operation = multiply
print(operation(5, 6))


"""
Поскольку функция в Python может представлять такое же значение как строка или число, 
соответственно мы можем передать ее в качестве параметра в другую функцию. Например, определим функцию,
 которая выводит на консоль результат некоторой операции:
 """

def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
 
def sum(a, b): return a + b
def multiply(a, b): return a * b
 
do_operation(5, 4, sum)         # result = 9
do_operation(5, 4, multiply)   # result = 20





"""Символ * позволяет установить, какие параметры будут именнованными - то есть такие параметры, 
которым можно передать значения только по имени. 
Все параметры, которые располагаются справа от символа *, 
получают значения только по имени:"""


"""Если наоборот надо определить параметры, 
которым можно передавать значения только по позиции, 
то есть позиционные параметры, 
то можно использовать символ /: все параметры, 
которые идут до символа / , являются позиционными и 
могут получать значения только по позиции"""


"""Для однойфункции можно определять одновременно позиционные и именнованные параметры"""


def print_person(name, /,  age = 18, *, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")

 

 
print_person("Sam", company ="Google")               # Name: Sam  Age: 18  company: Google
print_person("Tom", 37, company ="JetBrains")        # Name: Tom  Age: 37  company: JetBrains
print_person("Bob", company ="Microsoft", age = 42)
print_person("Sam",34,company="sadssd")