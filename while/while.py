# x=8
# i=1
# while i<x:
#     print(x)
#     i+=i
#     if i<=x:
#         break
#     x-=1


# x=4

# while x<10:
#     if x==5:
#         continue
        
#     x+=1
#     print(x)
    
# else:
#     print("nehcego")    

#task
def summm(n):
 
    suma = 0
 
    while n > 0:
        digit = n % 10
        suma = suma + digit
        n = n // 10

    print(suma)
    return suma

summm(421)

# y=8910

# y=y//10
# print(y)

number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, переходим к новой итерации цикла
        continue
    print(f"number = {number}")



"""
N = 81
print('N = ', N)

while N >= 3:
    N /= 3
print("Является степенью 3: ", (N==1))"""




#
"""import random

A = random.randrange(50,100)
B = random.randrange(1,A)
print('A = ', A)
print('B = ', B)

r = A - B
while r >= B:
    r -= B
    print(r,"-",B)
print("Остаток: ", r)"""