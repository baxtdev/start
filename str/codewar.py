data=str(input("Add:"))
array=[]
for counter,i in enumerate(data):
    if i.isupper():
        counter
    elif data.count(i)>1:
        array.insert(counter,")")
    elif data.count(i)==1:
        array.insert(counter,"(")
    print(counter)

data=''.join(array)
print(data)

a=2
b=5
summ=int(a)+(b)
binar=bin(summ)[2:]
print(binar)

def search_bigast(numbers:str):
    result=[]
    maxAndMin=[]
    data=numbers.split()
    for el,i in enumerate(data):
        result.append(int(i))
    max_el=max(result)
    min_el=min(result)
    maxAndMin.insert(0,max_el)
    maxAndMin.insert(1,min_el)
    all_res=" ".join(map(str,maxAndMin))
    return all_res


def printer_error(s):
    error_count = sum(1 for char in s if char not in 'abcdefghijklm')    
    return f"{error_count}/{len(s)}"


def filter_list(l:list):
    a=list(x for x in l if type(x) is int)
    print(a)


def square_digits(number:int):
    number=str(number)
    result=list(int(x)**2 for x in number)
    result="".join(map(str,result))
    return int(result)



