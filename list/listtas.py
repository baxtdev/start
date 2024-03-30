# array=[12,12]
# print(array)
"""itaration array"""
# i=0
# while i<len(array):
#     print(array[i])
#     i+=1

"""summa array"""

# summ=0

# for i in array:
#     summ+=i
# print(summ)    

# count=0
# summ=0
# while count<len(array):
#     summ+=array[count]
#     count+=1
# print(summ)    

"""min and max element array"""
a=[9,3,-8,5,-28,6,-1]
max_element=0
min_element=a[0]
for i in a:
    if i>max_element:
        max_element=i
    elif min_element>i:
        min_element=i
print("max",max_element,"min_el",min_element) 

"""min element array"""
min_el=a[0]       
for i in range(len(a)):
    if min_el>a[i]:
        min_el=a[i]
# print(min_el)   
summ=0
for i in a:
    summ+=i

array_desc=[]
for i in a:
    if i<0:
        array_desc.append(i)
        a.remove(i)        
print("list+",a,"list-",array_desc)

a=[9,3,-8,5,-28,6,-1]

"""sum indexes array
"""
summa=0
for i in a:
    # print(f"index.({i}):",a.index(i))
    if a.index(i)%2==0:
        summa+=a.index(i)
        print(summa-a.index(i),"+",a.index(i),"=",summa)


print(summa)     


# for i in range(len(a)-1,-1,-1):
    # print(a[i])

# summ_x=summ/len(a)
# print(summ,summ_x)    

# a=8.6489
# print(round(a,2))            
