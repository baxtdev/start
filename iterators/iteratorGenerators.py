#iterator
"""Итератор для перебора набора данных такие как список,кортеж,множество,словарь он имеет элемент для итерации 
мы можемм увидеть в class MyNumbers метод iter ,next iter это элэмент для перебора next каждый раз вызывает следующую итерацию
"""
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#generator
"""Генерптор работает с итерациям но в генераторе мало кодов и боле легче итерацию можем понять"""
def my_numbers():
  a = 1
  while True:
    yield a
    a += 1
 
mygen = my_numbers()
 
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
