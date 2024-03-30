#Удвоение чисел:
doubled_numbers = [x * 2 for x in range(1, 11)]

#Квадраты четных чисел:
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

#Фильтрация гласных:
vowels = [char for char in "hello world" if char in "aeiou"]

#Четные числа от 1 до 20:
even_numbers = [x for x in range(1, 21) if x % 2 == 0]

#Длины слов:
sentence = "The quick brown fox jumps over the lazy dog"
word_lengths = [len(word) for word in sentence.split()]

print(word_lengths)


#Фильтрация положительных чисел:
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]
negative_numbers = [x for x in numbers if x < 0]

#Подсчет четных и нечетных чисел:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]

#Уникальные элементы:
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))

