try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except Exception as e:
    print(e)
    print("Преобразование прошло неудачно")
else:
    print("Hello man")
finally:
    print("Aplication is close")



a=0

if a==0:
    raise ValueError("Этот обьект равен нулю")

else:
    print("этот обект не равен нуля")
