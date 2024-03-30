# guests = ['Родители', 'Одноклассники', 'Лида и Наташа']
# print(guests)  # ['Родители', 'Одноклассники', 'Лида и Наташа']
# guests.pop(0)
# print(guests)  # ['Родители', 'Одноклассники']
# guests.append('Дима')
# guests.append('Света')
# print(guests)

"""Для добавления элемента применяются методы append(), extend и insert, а для удаления - методы remove(), pop() и clear()."""

people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
 
slice_people1 = people[:3]   # с 0 по 3
# print(slice_people1)   # ["Tom", "Bob", "Alice"]
 
slice_people2 = people[1:3]   # с 1 по 3
# print(slice_people2)   # ["Bob", "Alice"]
 
slice_people3 = people[1:6:2]   # с 1 по 6 с шагом 2
# print(slice_people3)   # ["Bob", "Sam", "Bill"]

array=[1,2,3,4,5,6,'gucci','hushu']
lenght=len(array)
item_count=array.count(1)#коичество 1 внутри списка
item_index=array.index('gucci')#индек элемента gucci
array.insert(0,'name')# добавляет элемент item в список по индексу index
array.append(True)    # добавляет элемент item в конец списка
second_arr=[2,3,'gabarid',False,True]
array.extend(second_arr)# добавляет набор элементов items в конец списка
array.remove('hushu') # удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError
array.pop(6)#удаление элемента по инлексу
print(array)
array=['budo','adbu']
array.sort()
print(array)

kortej=tuple(range(5))
print(kortej)
# a2 = [i*2+1 for i in range(9)]
# print(a2)
# print(kortej)
