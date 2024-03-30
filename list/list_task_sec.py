"""Изменение списка:
Напишите программу, которая изменяет исходный список, 
заменяя все отрицательные элементы на их квадраты,
 а положительные - на их кубы."""

a=[-21,-1,1,31]

for i in a:
    if i<0:
        print(a[a.index(i)],"**2",a[a.index(i)]**2)
        a[a.index(i)]=a[a.index(i)]**2
        
    else:
        print(a[a.index(i)],"**3",a[a.index(i)]**3)
        a[a.index(i)]=a[a.index(i)]**3
print(a)          

print(a)
b=[1,1,1,1,9,1,1,1]

el=b[0]
for i in b:
    if i==el:
        el=i
    else:
        print("ne ravno")
print(el)        