class BankAkount:
    def __init__(self,owner,password=1234) -> None:
        self.__owner=owner
        self.__blance=0
        self.__password=password
        print("Счет в банке создался")

    def get_balance(self,password):
        if self.__password==password:
            print(f"{self.__owner} ваш баланас {self.__blance} сом")
        else:
            print("Не правильный пароль")

    def set_balance(self,balance,password):
        if self.__password==password:
            if balance>0:
                self.__blance+=balance
                print("Ващ текузий баланс",self.__blance)
            else:
                print("Пожалуйста проверте данные котрые вы ввели")
        else:
            print("Не правильный пароль")


    def change_paswsword(self,old_password,new_password):
        if self.__password==old_password:
            self.__password=new_password
            print(f"{self.__owner}, ваш пароль изменено")
        else:
            print(f"Вы ввели не правилный старый пароль")

tom=BankAkount("Tomas")    
tom.get_balance(1234)
tom.set_balance(200,1234)


