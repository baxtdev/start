# for i in 1,4,5,6:
#     print(i**2)

# for i in range(1,10,1):
#     print(i)

# rows = int(input("Enter the rows"))  
# for i in range(0,rows+1):  
#     for j in range(i):  
#         print("*",end = '')
#     print()   
       

# col = int(input("Введите число"))
# for i in range(10,1,-2):
#     print(i)

# a='asdads'
# print(len(a))
# summ=0
# for i in range(len(a)):
#     summ+=i

# print(summ)    




# x=1
# for i in range(10):
#     if i==5:
#         continue
#     print(i)
#     x+=1


# print("reult",x)    
    
# for el in range(1,10):
#     print(el)    

# print(list(range(2, 10, 2)))
name="hushbaht"

# print(name[::-1])

if "a" in name:
    print(name.index("a"))


text = "Python is a powerful programming language. It is used for various purposes."

# Разделение на предложения
sentences = text.split('.')
for sentence in sentences:
    # Определение количества слов
    words = sentence.split()
    num_words = len(words)
    print(f"Предложение: '{sentence.strip()}', Количество слов: {num_words}")


