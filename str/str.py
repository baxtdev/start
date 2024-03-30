# name = input("Enter your name:\n")

# #строка состоит только из алфавитных символов
# if name.isalpha():
#     print("Name is ok",name)
# else:
#     print("name is valueror")    

# возвращает True, если все символы строки - цифры
# if name.isdigit():
#     print("ther are only numbers",name)
# else:
#     print("your name",name)

# возвращает True, если строка начинается с подстроки str
# if name.startswith("name"):
#     print("your",name)

# else:
#     print("non",name)    

# text="My name is xushu"
# splitted_text = text.split()

# print(splitted_text,end="*",sep="2")
# for i in splitted_text:
#     print(i,i,i,sep="na")

# file = open('txt.py','a+')


# def value(items):
#     for item in items:
#         print(item, file=file,end=" , ")
#     file.close()

# value([1,2,3,4,5,6,7,8,9,10])

#связывает 
# def new_func(myTuple):

#     x = "".join(myTuple)

#     print(x)


# names = ["xu","shb","aht"]
# names2= ["x","ush","baht"]

# new_func(names2)


# x="".join(names)
# y="".join(names2)
# if x==y:
#     print("равен")



# txt = "Today is my first day with python!"
# if "python" in txt:
#   print("really?....")
#   x=input("???")
#   print("okkkkkkaaaayyyy")
# else:
#   print("soooo")  


b = "xushu"
print(b[::-1])
value = int(123456)

# value=str(value)
# value=int(value[::-1])
# print(type(value))


two_plus_three = 2 + \
3
# print(two_plus_three)

# def reverse_number(n):
#     r = 0
#     while n > 0:
#         r *= 10
#         r += n % 10
#         n /= 10
#     return r

# print(reverse_number(123))


# u2 = 'Еще пример'.encode('utf-8')
# print(u2)
# u1 = '\u043f\u0441\u0442\u0443\u0435\u0442' # привет
# print(u1)

# decode=b'\xd0\x95\xd1\x89\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x80'.decode('utf-8')
# print(decode)

# S = 'spam"s'
# # S = "spam's"
# S = r'C:\newt.txt'

# print(S)



# Объединение строк
string1 = "Hello"
string2 = "World"
combined_string = string1 + " " + string2
# print(combined_string)

# Изменение регистра
inverted_case_string = combined_string.swapcase()
# print(inverted_case_string)

# Замена символов
replaced_string = combined_string.replace("l", "L")

# print(replaced_string)


sentence = "This is a sample sentence."

# Разделение на слова
words = sentence.split()

print("errr",words)


# Замена слова
replaced_sentence = sentence.replace("sample", "modified")


print(replaced_sentence)


my_string = "Python"
ari="1222121"

# Перебор каждого символа и вывод индекса
for index, char in enumerate(my_string):
    print(f"Символ {char} имеет индекс {index}")


a=" "