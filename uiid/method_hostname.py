import uuid

# Определение кортежа из двух имен хостов
hostname =('www.andreyex.ru', 'www.google.com')

# Итерировать значения кортежа, используя цикл
# Распечатать имя хоста
print("Hostname: ", hostname)
# Используйте uuid5(), чтобы получить значение SHA-1
print('\t Значение SHA-1:', uuid.uuid5((uuid.NAMESPACE_DNS, hostname[0])))
# Используйте uuid3() для получения значения MD5
print(' \t Значение MD5: ', uuid.Uuid3((uuid. NAMESPACE_DNS, hostname[1])))