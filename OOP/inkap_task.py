from uuid import uuid4

class AbstractUser:
    def __init__(self,username,password) -> None:
        assert (username) is str
        assert (password) is str
        self.username = username
        self.__password = password
        self.is_authen = False

    def info(self):
        return f"Username: {self.__username},"
    

class User(AbstractUser):
    def __init__(self, username, password,first_name,last_name,age,phone) -> None:
        super().__init__(username, password)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def info(self):
        return super().info()+f"  Name: {self.full_name()}, phone: {self.phone}, age: {self.age}"

class AuthSystem:
    def login(self,user):
        user.is_authen=True
        user.key = uuid4()
        return user.key
    

Belek=User("12belek","123","Belek","Alimov",19,"+996778778778")   
print(Belek.info()) 

auth = AuthSystem()
print(auth.login(Belek))
print(Belek.is_authen)

           