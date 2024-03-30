def open_file_for_add(path:str,date:list):
    with open(path,"a") as my_file:
        if type(date) is list:
            for i in date:     
                my_file.write(i)
            print("Запсиь закончилась")    
        else:
            print("Произошло ошибка")



def open_file_for_read(path:str):
    with open(path,"r") as file:
        for data in file:
            print(data,end="")



def open_file_for_del(path:str):
    with open(path,"w") as file:
        file.write("")

        

FILENAME = "messages.txt"
messages = list()
 
for i in range(4):
    message = input("Введите строку " + str(i+1) + ": ")
    messages.append(" "+message + "\n")

# open_file_for_del(FILENAME)
open_file_for_add(FILENAME,messages)

open_file_for_read(FILENAME)
