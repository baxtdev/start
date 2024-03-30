import os
import random
#create folder
# os.mkdir("/home/xushu/study_plan_python/start/files/model_os/models")

# #del folder
# os.rmdir("models")

# #rename folder name
# os.rename("models","folder_for_os")

#has is file ?

# x=os.path.abspath("folder_for_os")
# a=open(f'{x}'+r'/text.txt',"w").write('укщщщ')
# print(x)




secret_number = random.randint(1, 10)

count=4
while 4>0:
    chislo=int(input("goo"))
    if secret_number==chislo:
        print("Угадали")
        break
    else:
        if chislo<secret_number:
            print("ваше число меньше")
        elif chislo>secret_number:
            print("ваше число больше")    
        else:
            print("вашше не близко")