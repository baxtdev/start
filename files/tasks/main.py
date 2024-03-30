import json

data_to_write = {"name": "Alice", "age": 25, "city": "Wonderland"}

def add(data:list):
    with open("output.json", "w") as json_file:
        json.dump(data, json_file, indent=2)
        return "Добавлено"

def read():
    with open("output.json", "r") as json_file:
        data_read = json.load(json_file)
        return data_read['age']

# add(data_to_write)
print(read())