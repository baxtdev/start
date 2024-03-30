#принимаем два целые числа и выводим все существующий число между ними в порядке убывание

"""B = int(input("B:\n"))
A= int(input("A:\n"))

print('A = ', A)
print('B = ', B)
N = 0
for i in range(B-1, A, -1):
    print(i,end=' ')
    N += 1
print()
print("N = ", N)    
"""

# у нас есть цена для кг конфета и ы должны найти цена от 1.2,1.4, до 2кг
"""price = 10 
print('Цена 1 кг конфет: ', price)
print()
for i in range(0,5):    
    x = 1.2 + 0.2*i
    print('Стоимость {0} кг: {1}'.format(x, x * price))
print()
"""

#выводит производные
"""A = 2
B = 4
print('A = ', A)
print('B = ', B)

P = 1
for i in range(A,B+1,1):
    P *= i
    print(i," : ",P)
print("Product = ",P)"""

#дано вещественное число A и целое число N. Найти A в степени N :
N = 64
print('N = ', N)
A = 2
print('A = ', A)

P = 1
for i in range(1,N+1):
    P *= A
    print(i," : ",P)
print("Product = ",P)




