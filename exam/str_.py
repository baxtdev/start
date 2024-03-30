from array_ import *

#Экранированные последовательности
a = "s\np\ta\nbbb"

#Неформатированные строки (подавляют экранирование)
b = r"C:\temp\new"

s="avcd"
s = s[0] + 'b' + s[2:]

d=",".join(s)

c=d.split(",")
print(c)


# Строки и методы
name_length = len(student1_name)  # Находим длину имени
upper_name = student1_name.upper()  # Преобразуем имя в верхний регистр
contains_substring = "ан" in student1_name  # Проверяем, содержит ли имя подстроку "ан"
capitalized_name = student1_name.capitalize()  # Заменяем первую букву имени на заглавную
