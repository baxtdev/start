print(f"выберите один из вкладок\n\t1:register\n\t2:login\n\t 3:reset password")
menu=int(input("Выберите:"))
employe_list={"Arzy":{"password":"Qwerty2004","number":"+99676767676"}}
while menu!=0:
    if menu==1:
        register=str(input("Введите Login:\n"))
        search_user=employe_list.get(register)
        if not register.isnumeric() and search_user is None:
            print("Пароль должен иметь и буквы и число")
            password=str(input("Введите пароль"))
            if password.isdigit(): 
                print("Поле password  имееть толко цифры")
                print(f"выберите один из вкладок\n\t1:register\n\t2:login\n\t 3:reset password\n\t 0:quit")
                menu=int(input("Выберите:"))
            
            else:
                if password.isalpha():
                    print("Парол не польностью безопасный так как оно состоится только из буквы")
                    print(f"выберите один из вкладок\n\t1:register\n\t2:login\n\t 3:reset password\n\t 0:quit")
                    menu=int(input("Выберите:"))

                else:    
                    if 8==len(password) and password!=password.lower() and password!=password.upper():
                        number=str(input("Введите номер телефона с кодом страны +996"))
                        if "+996" in number:
                            employe_list[register]={'password':password,'number':number}
                            print("вы успешно зарегистрировались",employe_list.get(register))
                            print(f"выберите один из вкладок\n\t1:register\n\t2:login\n\t 3:reset password\n\t 0:quit")
                            menu=int(input("Выберите:"))
        else:
            print("Пользователь с таким именнем уже существует")
            print(f"выберите один из вкладок\n\t1:register\n\t2:login\n\t 3:reset password\n\t 0:quit")
            menu=int(input("Выберите:"))
        
    elif menu==2:
        login=str(input("Login:\t"))
        password_login=str(input("password:\t"))
        get_user=employe_list[login]['password']
        if login and get_user==password_login:
            print("login sucsesfull",get_user)
            print(f"выберите один из вкладок\n\t1:register\n\t2:login\n\t 3:reset password\n\t 0:quit")
            menu=int(input("Выберите:"))
    
        else:
            print("error")
            print(f"выберите один из вкладок\n\t1:register\n\t2:login\n\t 3:reset password\n\t 0:quit")
            menu=int(input("Выберите:"))

    elif menu==3:
        username=str(input("Login:\t"))
        number=str(input("Number:\t"))
        get_reset=employe_list[username]['number']
        if get_reset==number:
            print("ypur password",employe_list[username]['password'])
            print(f"выберите один из вкладок\n\t1:register\n\t2:login\n\t 3:reset password\n\t 0:quit")
            menu=int(input("Выберите:"))

        else:
            print("your login or number not found")    
            print(f"выберите один из вкладок\n\t1:register\n\t2:login\n\t 3:reset password\n\t 0:quit")
            menu=int(input("Выберите:"))

else:
    print("Вы закрыли програму")


