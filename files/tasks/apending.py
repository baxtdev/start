import json

with open("existing_data.json", "r") as json_file:
    existing_data = json.load(json_file)

new_data = {"name": "Charlie", "age": 35, "city": "Charm City"}
existing_data.append(new_data)

with open("existing_data.json", "w") as json_file:
    json.dump(existing_data, json_file, indent=2)
