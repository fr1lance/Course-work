import json
import copy

file = open("default_settings.json", encoding='utf-8')
json_data = json.load(file)
file.close()

print("Введите количество комнат")
json_data["room"]["number"] = int(input())
for i in range(json_data["room"]["number"]):
    print("Введите ширину комнаты в метрах", i+1)
    json_data["room"]["weight"].append(float(input()))
    print("Введите длину комнаты в метрах", i + 1)
    json_data["room"]["length"].append(float(input()))
    print("Введите высоту комнаты в метрах", i + 1)
    json_data["room"]["height"].append(float(input()))

print("Введите время эмулирования в секундах")
json_data["general"]["time_for_work"] = int(input())

print("Введите начальную температуру")
json_data["climate"]["start_temperature"] = float(input())
print("Введите поддерживаемую температуру")
json_data["climate"]["support_temperature"] = float(input())

print("Есть ли в доме кондиционер? (y/n)")
if input() == "y":
    print("Введите количесвто кондиционеров")
    json_data["climate"]["conditioner"]["number"] = int(input())
    print("Введите мощность одного кондиционера")
    json_data["climate"]["conditioner"]["power"] = float(input())
    print("Введите производтельность по холоду одного кондиционера")
    json_data["climate"]["conditioner"]["frozen_power"] = float(input())
else:
    print("Окей, кондиционера нет")
    json_data["climate"]["conditioner"]["number"] = 0
    json_data["climate"]["conditioner"]["power"] = 0
    json_data["climate"]["conditioner"]["frozen_power"] = 0

print("Есть ли в доме обогреватель? (y/n)")
if input() == "y":
    print("Ваедите количесвто обогревателей")
    json_data["climate"]["heater"]["number"] = int(input())
    print("Введите мощность одного обогревателя")
    json_data["climate"]["heater"]["power"] = float(input())
else:
    print("Окей, обогревателей нет")
    json_data["climate"]["heater"]["number"] = 0
    json_data["climate"]["heater"]["power"] = 0


tmp_device = copy.deepcopy(json_data["device_templete"])

print("Есть ли в доме другие устройства? (y/n)")
if input() == "y":
    print("Сколько их?")
    for i in range(int(input())):
        tmp_device = copy.deepcopy(json_data["device_templete"])
        print("Введите имя устройства")
        tmp_device["name"] = input()
        print("Введите мощность устройства")
        tmp_device["power"] = float(input())
        print("Введите количество запусков устройства")
        tmp_device["number_of_starts"] = int(input())
        for tmp_number in range(tmp_device["number_of_starts"]):
            print("Введите время включения", tmp_number+1)
            tmp_device["time_for_start"].append(int(input()))
            print("Введите время выключения", tmp_number + 1)
            tmp_device["time_for_end"].append(int(input()))
            tmp_device["spent_energy"]=0
        json_data["devices"].append(tmp_device)
        tmp_device = None

else:
    print("Окей, других устройств нет")

print("Нужно ли эмулировать открытие форточек (y/n)")
if input() == "y":
    print("Введите количество открытий форточек")
    for i in range(int(input())):
        print("Введите время открытия форточки №", i)
        json_data["opening_window"]["time_for_open"].append(int(input()))
    print("Введите изменение температуры в градусах при открытии форточки")
    json_data["opening_window"]["delta_temperature"] = float(input())
else:
    print("Ок. Эмулирования открытия форточек не будет")


with open('settings.json', 'w', encoding='utf-8 ') as file_for_write:
    file_for_write.write(json.dumps(json_data, indent=4))



