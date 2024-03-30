from array_ import *
from set_ import *
from dict_ import *
from str_ import *
 # Удаляем последнюю оценку

# Кортеж
name_tuple = tuple(student1_name)  # Преобразуем имя в кортеж
reversed_name = ''.join(reversed(name_tuple))  # Разворачиваем имя
combined_tuple = name_tuple + tuple(reversed_name)  # Объединяем кортежи
index_of_a = name_tuple.index('а')  # Находим индекс первой 'а' в имени
substring_tuple = name_tuple[1:4]  # Получаем подкортеж от второго до четвертого элемента


# Множество


# Вывод результатов
print("Массив (список):", grades_list, grades_sum)
print("Кортеж:", name_tuple, reversed_name, combined_tuple, index_of_a, substring_tuple)
print("Словарь:", grades_dict, names_dict)
print("Множество:", grades_set, is_subset)
print("Строки и методы:", name_length, upper_name, contains_substring, capitalized_name)
