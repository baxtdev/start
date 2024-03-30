# # Задача 1: Создайте словарь, где ключи - числа от 1 до 5, значения - квадраты этих чисел
# squares_dict = {x: x**2 for x in range(1, 6)}
# # Задача 2: Оставьте только элементы с четными значениями в словаре
# numbers_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# even_numbers_dict = {key: value for key, value in numbers_dict.items() if value % 2 == 0}
# # Задача 3: Объедините два словаря
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# merged_dict = {**dict1, **dict2}

# name = str(input('name'))
# age = int(input('age'))
# number = str(input('number'))

# employe={}

# employe[name]={'age':age,'number':number}
# print(employe)

user_list={}
def user_contacts(user_array:list):
    print(user_array)
    if type(user_array) is list:
        for array in user_array:
            if len(array)>1:
                
                user_list[array[0]]=array[1]   
            elif len(array)==1:
                user_list[array[0]]=None

a=[['miko','12'],['hardin','1'],['tom']]



user_contacts(a)
print(user_list)