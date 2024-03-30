age = int(input("Введите возраст:\n"))
name = input("Введите имя:\n")
height = float(input("Введите рост в см:\n"))
weight = float(input("Введите вес в кг:\n"))


def new_func(age, name, height, weight):
    if name.isalpha() and age and height and weight:
        if 18 <= age <= 25 and 170 <= height <= 200 and 50 <= weight <= 100:
            print(f"{name}, вы пригодны для службы в армии!")
    
        else:
            print(f"{name}, к сожалению, вы не пригодны для службы в армии. Причина:")

            if age < 18:
                print("Ваш возраст меньше минимального для службы в армии.")
            elif age > 25:
                print("Ваш возраст превышает максимальный для призыва в армию.")

            if height < 170 or height > 200:
                print("Ваш рост не соответствует требованиям.")

            if weight < 50 or weight > 100:
                print("Ваш вес не соответствует требованиям.")
    else:
        print("Пожалуйста проверите у вас данные не правильно")

new_func(age, name, height, weight)
    

