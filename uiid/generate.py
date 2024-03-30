import uuid

# Создайте список идентификаторов допустимого формата
list_Ids = [
'a4f8dd97-c8be-345b-239e-8a68e6abf800',
'dcbbaa88-5bf1-11dd-ab48-990ab200d674',
'4567aabb-89ad-77ab-67ad-aaaccdd904ae'
]

# Распечатать значения списка с помощью цикла
print(' \n Значения списка: ')
for val in list_Ids:
    print (val)

# Значения списка будут преобразованы в uuid и отсортированы
try:
    uuids = [ uuid.UUID(s) for s in list_Ids ]
    uuids.sort()
    print(' \ n Значения отсортированных uuids:')
    for val in uuids:
        print (val)
    
except ValueError:
# Распечатать сообщение об ошибке, если какое-либо значение списка находится в недопустимом формате
    print('Плохо сформированный шестнадцатеричный UUID')