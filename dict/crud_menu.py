category={1:"breakfast",
          2:"foods"
}

foods={
    "pizza":{
        "cat_id":1,
        "price":234
    }
}



CHOICE=f"""
    1:"Добаление товара,
    2:"Измнение товара,
    3:"Удаление товара,
    4:"Список товара,
    5:"Категория товара,
    6:"Добавление категории,
    0:"Exit","""

print("Выберите один из вариантов",CHOICE)
menu=int(input("Выбор:\t"))

while menu!=0:
    print("Вы выбрали вариант добавление товара")
    if menu==1:
        name=str(input("Название товара:\t"))
        if not name in foods:    
            print(category)
            category_id=int(input("category_id:\t"))
            if category_id in category:    
                rpice=int(input("цена:\t"))
                if not name in foods:
                    foods[name]={"category_id":category_id,"price":rpice}
                    print("Товар успешно добавлен",foods[name])
                    print("Выберите один из вариантов",CHOICE)
                    menu=int(input("Выбор:\t"))
            else:
                print("Нету такой категории")
                print("Выберите один из вариантов",CHOICE)
                menu=int(input("Выбор:\t"))
        else:
            print(f"Товар с таким названием уже существует{foods[name]}")  
            print("Выберите один из вариантов",CHOICE)
            menu=int(input("Выбор:\t"))  

    elif menu==2:
        print("Вы выбрали вариант добавление товара")
        print("Какой товара вы хотите изменить")
        print(list(x for x in foods))
        name_fod=str(input("Напиши название товара"))
        print(foods.get(name_fod))
        print(category)
        category_edit=int(input("Введите новую категорию для товара"))
        if category_edit in category:
            price_edit=int(input("Введите новую цену для товара"))
            foods[name_fod]['category_id']=category_edit    
            foods[name_fod]['price']=price_edit
            print(foods[name_fod])    
            print("Выберите один из вариантов",CHOICE)
            menu=int(input("Выбор:\t"))
        else:
            print("Нету такой категории")
            print("Выберите один из вариантов",CHOICE)
            menu=int(input("Выбор:\t"))
    elif menu==3:
        print(list(x for x in foods))
        name_del=str(input("Введите один из имя товара с  верхной списки"))
        if name_del in foods:
            foods.pop(name_del)
            print(f"Товар, {name_del} удалено")
            print("Выберите один из вариантов",CHOICE)
            menu=int(input("Выбор:\t"))
        else:
            print(f"товар с таким название не существуе : {name_del}")
            print("Выберите один из вариантов",CHOICE)
            menu=int(input("Выбор:\t"))