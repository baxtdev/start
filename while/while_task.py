login=str(input("login: "))

password=str(input("password: "))


def valid_password(password:str):
    count=4
    while password!="password2":
        print(f"your password invalid\n у вас есть {count} попытки")
        password=input("pasword:")
        count-=1
        if count==0:
            print("У вас не осалось попытки")
            return
    else:
        print("your passsword is correct")    
 
        return 
    
valid_password(password)


# def reverse_number(n):
#     r = 0
#     while n > 0:
#         r *= 10
#         r += n % 10
#         n /= 10
#     return r

# print(reverse_number(123))

