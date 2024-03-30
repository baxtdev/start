import json

data=[
    {
        "id":2,
        "name":"Andy",
        "age":19
    },
    {
        "id":3,
        "name":"Habibi",
        "age":21
    }
]

with open('tom.json','w') as users:
    
    users_data=json.dump(data,users,indent=4)
    
with open('tom.json','r+') as json_f:
    data=json.load(json_f)    
for i in range(len(data)):
    print(data[i]['name'])

    
