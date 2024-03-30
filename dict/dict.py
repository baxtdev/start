users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)
# print(users_dict)



users = {
    11111111: "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
# получаем элемент с ключом "+11111111"
# print(users[11111111])      # Tom
 
# установка значения элемента с ключом "+33333333"
users["+33333333"] = "Bob Smith"
# print(users["+33333333"])   # Bob Smith


users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
user1 = users.get("+55555555")
# print(user1)    # Alice
user2 = users.get("+33333333", "Unknown user")
# print(user2)    # Bob
user3 = users.get("+44444444", "Unknown user")
# print(user3) 


users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
key = "+55555555"
user = users.pop(key)
# print(user)     # Alice
 
user = users.pop("+4444444", "Unknown user")
# print(user)     # Unknown user



users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}




# for key, value in users.items():
#     print(f"Phone: {key}  User: {value} ")




lit_dict={}
def fuunc(**key_value):
    for i,zl in key_value.items():
        lit_dict[i]=zl

fuunc(**users)
print(lit_dict)

lit_dict['news_key']="Value"
lit_dict.pop('news_key')
# print(lit_dict)

# for count,i in enumerate(lit_dict.values()):
#     print(count,i)
name=['id','name','sioname']
_name=1

lit_dict=dict.fromkeys(name,_name )
print(lit_dict)