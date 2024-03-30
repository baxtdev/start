a=b=c= 1

print(a)
bank_accounts={"Tom":{
    "balance":1000,
    "interest_rate":0.10,
    "year":5
},
"Alisa":{
    "balance":1020,
    "interest_rate":0.10,
    "year":6
}}



def bank(user_info,user_name):
    try:
        user_one=user_info[user_name]
        interest_rate = user_one["interest_rate"]
        years=user_one["year"]
        balance=user_one["balance"]
        for year in range(years):
            balance += balance * interest_rate

        user_one['balance']=balance
        return user_one['balance']
    
    except ValueError:
        print(f"Нету такого пользователя{user_name}")
        return None
    
    except KeyError as e:
        print(e)

    finally:
        print("Программа закрыто")

# name = str(input("Введите имя пользователя: "))
# result =bank(bank_accounts, name) 
# print(f"Конечный баланс для пользователя Tom после срока вклада: {result} рублей")


