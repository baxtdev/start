from array_ import *

grades_set = set(grades_list)  # Создаем множество из оценок
grades_set.add(87)  # Добавляем новую оценку
grades_set.intersection_update({85, 92, 95})  # Находим пересечение с другим множеством
is_subset = grades_set.issubset({85, 92, 95})  # Проверяем, является ли множество подмножеством другого
