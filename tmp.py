import json

file = open("settings.json", encoding='utf-8')
json_data = json.load(file)
file.close()
print(json_data["devices"][0])