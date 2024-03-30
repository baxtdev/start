login=str(input("login\n"))

if login.isalpha()and len(login)<=8:
    password=str(input("password\n"))
    if ('*' in password) or ('-' in password) or ('#' in password):
        print("Поля password имееть не допустимые символи*#-")
    else:
        if password.isdigit(): 
            print("Поле password  имееть толко цифры")  
        else:
            if password.isalpha():
                print("Парол не польностью безопасный так как оно состоится только из буквы")
            else:    
                if 8==len(password) and password!=password.lower() and password!=password.upper():
                    print("Ypour password is correct")
                else:
                    print("Пверьте еще раз свой пароль")
else:
    print("Логин имеет не доупстимые символы 134*#-")                



# print(password.upper())    
        





# print(allowed_sym)



# str_name="hushbaht"
# summ=0
# a="h"

# for i in str_name:
#     if i==a:
#         print(a,"==",i)
#         summ=summ+1

# print("COL",summ)    # print(i,end="")



# hello_text=input("go text")

# while hello_text=="yes":
#     hello_text=input("really???")