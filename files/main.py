def open_file(path:str):
    try:    
        my_file=open(path,"+r")
        
        try:
            a=list()
            for i in my_file:
                a.append(i+'\t')
            print(a)
            menu=int(input("choice\n1:add\n2:exit"))
            if  menu==1:
                text_input=str(input("Введите текст"))
                my_file.write(text_input)
                
            else:
                my_file.close()
                print("програма exit")

        except:
            print("Произошло ошибка при прочитени файла")
            my_file.close()
            print("Файл закрылся")
    
    except:
        print("Произошло ошибка при открытыя файла")
    
    finally:
        print("Программа перестала")    

def write_file(path:str):
    try:    
        my_file=open(path,"w")
        
        try:
            for i in my_file:
                a=["Almanani ","lionel"]
                a.remove("lionel")
            _date=input("""
                        Напишите текст чтобы внелрит это на ваш файл
                        """)
            my_file.write(_date)
            my_file.close()
        
        except Exception as e:
            print("Произошло ошибка при записа файла",e)
            my_file.close()
            print("Файл закрылся")
    
    except Exception as ex:
        print("Произошло ошибка при открытыя файла",ex)
    
    finally:
        x=open(path)
        print("Программа перестала",x.readline()) 
        x.close()



# open_file("request.txt")
# write_file("request.txt")