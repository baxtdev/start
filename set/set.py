users = {"Tom", "Bob","Alice", "Tom","Tom",12}
users.add('Tobbi')

userSet={12,"Alice",'Oroz'}
print(userSet.remove(12))
print("userset",userSet)
print("Set",userSet.issubset(users))#возвращает True, если t содержит множество s
print(users.issuperset(userSet))
print(users.union(userSet))
print(users.intersection(userSet))
print(users.difference(userSet))
