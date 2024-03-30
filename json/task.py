"""У нас есть спсиок подростоков с дата рождении нам надо чтобы 
наша программа вместе год рождении 
оставил их возраст смотря на нынешний год"""
import json

# list_user=[
    
#     {   "id":0,
#         "name": "Andrey",
#         "bd": 2001
#     },
#     {   
#         "id":1,
#         "name": "Ali",
#         "bd": 2004
#     },
#     {   
#         "id":2,
#         "name": "Andrie",
#         "bd": 2003
#     },
#     {
#         "id":3,
#         "name": "Venom",
#         "bd": 2000
#     },
#     {
#         "id":4,
#         "name": "Sergo",
#         "bd": 2006
#     }
# ]


filename="childern.json"

def list_user_():
    with open(filename,'r+') as read_:
        data= json.load(read_)
        return data

def create(list_user):
    with open(filename,"w") as file:
        name = input("Введите имя :")
        age = int(input("введите возраст :"))
        list_user.append({"id":len(list_user),"name":name,"age":age})
        file.write(json.dumps(list_user,indent=4,ensure_ascii=False))      

def view():
    with open(filename,"r") as file:
        print("Вы выбрали метод List")
        data = json.loads(file.read())
        id=input(f"выберите id user{list(i for i in  range(len(data)))} :")
        if type(id) is str and id=="": 
            _object=data
        elif int(id)>=0<len(data):
            _object=data[id]
            
        print(_object)

def update():
    with open(filename,"r") as file:
        _object=json.load(file)
        print(_object)
        print("Вы в выбррали метод обновление")
        id=int(input("введите id-пользователья :"))
        print(_object[id])
        name=str(input("Введите новое имя "))
        age=int(input("Введите новый возраст"))
        if name and age:
            _object[id]['name']=name
            _object[id]['bd']=age
            with open(filename,"w") as newfile:
                newfile.write(json.dumps(_object,indent=4)) 

def delete():
    with open(filename,"r+") as file:
        _object=json.load(file) 
        id = int(input(f"Выберите id чтобы удалить {list(el for el in range(len(_object)))}"))
        print(_object[id])
        yes_or=input("yes or no")
        x=_object.pop(id) if yes_or=="yes" or "yes" else None
        if x:
            with open(filename,"w") as file_:
                json.dump(_object,file_,indent=4)

# create(list_user)
# update()         
# view()       
# delete()        