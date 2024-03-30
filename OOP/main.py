
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Создание объекта Person")
    
    def say_hello(self):
        print("hello")
    
    def say_word(self,message):
        print(f"Я скажу {message}")

    def displey_info(self):
        print(f"PersonName: {self.name}, PersonAge: {self.age}")


tom=Person("Hushu",34)
tom.say_hello()
tom.say_word("I love you")
tom.displey_info()