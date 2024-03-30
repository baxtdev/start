d = dict(short='dict', long='dictionary')
# print(d)

d = dict([(1, 1), (2, 4)])
# print(d)

d = dict.fromkeys(['a', 'b'], 100)
# print(d)

d = {a: a ** 2 for a in range(7)}

# print(d)

slov={"hushu":"2"
}
slov.setdefault("hushu2","name") 
# print(slov)

l='Hello, {2},{0},{1}!'.format('Vasya','hushu','342')
text="my secret is {sekret}-{first}".format(sekret="TOM",first="vASYA")

# print(text)

text="my secret is {hushu}-{hushu2}".format(**slov)
print(text)

import random

renadom_number=random.randint()
print(renadom_number)