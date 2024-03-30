# Примеры тернарного оператора

# 1. Проверка на четность
number = 10
result = "Even" if number % 2 == 0 else "Odd"

# 2. Проверка на положительное/отрицательное число
number = -5
result = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"

# 3. Фильтрация чисел
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]
filtered_numbers = [x if x > 0 else 0 for x in numbers]

# 4. Сравнение двух чисел
a, b = 5, 10
larger_number = a if a > b else b

# 5. Статус студента
score = 75
status = "Pass" if score >= 60 else "Fail"

# 6. Перевод чисел в строку
number = 42
number_as_string = str(number) if number > 0 else "Non-positive"

# Примеры list comprehension

# 7. Проверка на четность с использованием list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_or_odd = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

# 8. Удвоение чисел
doubled_numbers = [x * 2 for x in range(1, 11)]

# 9. Квадраты четных чисел
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

# 10. Фильтрация гласных
vowels = [char for char in "hello world" if char in "aeiou"]

nice=False
personality = ("вредная", "добрая")[True]
print(personality)