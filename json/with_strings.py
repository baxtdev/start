import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

object_dict=json.dumps(data,indent=4)
print(object_dict)


employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
employee_dict = json.loads(employee) 
print(employee_dict)

