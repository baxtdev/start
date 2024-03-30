# Напишите программу, которая принимает два множества от пользователя и проверяет, есть ли у них общие элементы.
# Пример:

set1 = {1, 2, 3}
set2 = {4, 5, 6}
# Ожидаемый результат: True


# Напишите программу, которая проверяет, являются ли два множества идентичными (имеют одни и те же элементы).
# Пример:
set1 = {1, 2, 3}
set2 = {3, 2, 1}
# Ожидаемый результат: True


# Напишите программу, которая проверяет, является ли одно множество подмножеством другого.
set1 = {1, 2}
set2 = {1, 2, 3, 4}
# Ожидаемый результат: True


# Напишите программу, которая проверяет, является ли одно множество надмножеством другого.
# Пример:
set1 = {1, 2, 3, 4}
set2 = {1, 2}
# Ожидаемый результат: True


# Напишите программу, которая объединяет несколько множеств.
# Пример:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
# Ожидаемый результат: {1, 2, 3, 4, 5, 6, 7}


# Напишите программу, которая находит пересечение нескольких множеств.
# Пример:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
# Ожидаемый результат: {3}


# Напишите программу, которая находит разность между одним множеством и несколькими другими.
# Пример:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
# Ожидаемый результат: {1, 2}


# Напишите программу, которая находит симметрическую разность двух множеств.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Ожидаемый результат: {1, 2, 4, 5}


# Напишите программу, которая объединяет одно множество с другими.
# Пример:
set1 = {1, 2}
set2 = {3, 4}
set1.update(set2)
# Ожидаемый результат: {1, 2, 3, 4}



# Напишите программу, которая изменяет первое множество, оставляя в нем только элементы, присутствующие в других множествах.
# Пример:
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
# Ожидаемый результат: {2, 3}