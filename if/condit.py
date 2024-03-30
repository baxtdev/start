print("Выберите пол:\n М \n Ж")
gender=str(input("ПОЛ:"))
category = 'site.com'

if gender == 'М':
    category = 'site.com/male'
    
elif gender == 'Ж':
    category = 'site.com/female'

# category = 'site.com/male' if gender == 'М' else 'site.com/female'

print(category)
# if gender == 'М':
#     category = 'site.com/male'
    
# elif gender == 'Ж':
#     category = 'site.com/female'



cont=5 if 5>4 or 4>6 else 6

print(cont)