def multiply(n): return lambda m: n * m
 
 
# fn = multiply(5)
# print(fn(3))        # 25
# print(fn(1))        # 30
# print(fn(2))


#or

def multiply(n):
    def inner(m): 
        return n * m
 
    return inner
 
 
# fn = multiply(4)
# print(fn(5))        # 25
# print(fn(6))        # 30
# print(fn(7))

def iterator():
    i=0
    def generator():
        nonlocal i
        i+=1
        return i
    return generator

iterator_=iterator()
print(iterator_())
print(iterator_())
print(iterator_())
print(iterator_())