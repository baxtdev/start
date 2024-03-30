#Умножение списка:
def multiply_list(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

# a=[2,3,3]
# print(multiply_list(a))
#max
def find_max(numbers):
    array=(x for x in numbers if type(x) is int)
    arr_l=list(array)
    return max(arr_l)

print(find_max([3,4,6,1,"sdsd",True
                
                ]))

#проверка на четность
def is_even(number):
    return number % 2 == 0


#раворачивание
def reverse_string(s):
    return s[::-1]


#слияние списка
def merge_lists(list1, list2):
    return list1 + list2


#palindrom
def is_palindrome(s):
    return s == s[::-1]


#Подсчет гласных в строке:
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


#Обратное слияние строк:
def reverse_merge_strings(str1, str2):
    return str1[::-1] + str2[::-1]


#Поиск уникальных элементов:
def find_unique_elements(lst):
    return list(set(lst))


#Среднее значение списка:
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

#Сортировка словаря по значениям:
def sort_dict_by_values(d):
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

