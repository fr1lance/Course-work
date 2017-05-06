import json
import copy

def chek_int(tmp_read):
    try:
        someVar = int(tmp_read)
        if someVar > 0:
            return(True)
        else:
            print("Это не целое или отрицательное число")
            return(False)
    except (TypeError, ValueError):
        print("Это не целое число")
        return(False)

def chek_int_end_time(tmp_read):
    try:
        someVar = int(tmp_read)
        if someVar > 0 and someVar <= json_data["general"]["time_for_work"]:
            return(True)
        else:
            print("Это не целое или отрицательное число")
            return(False)
    except (TypeError, ValueError):
        print("Это не целое число")
        return(False)


def chek_float(tmp_read):
    try:
        someVar = float(tmp_read)
        if someVar > 0:
            return(True)
        else:
            print("Это не дробное или отрицательное число")
            return(False)
    except (TypeError, ValueError):
        print("Это не дробное или отрицательное число")
        return(False)

def chek_float_temp(tmp_read):
    try:
        someVar = float(tmp_read)
        return(True)
    except (TypeError, ValueError):
        print("Это не дробное число")
        return(False)

try:
    file = open("default_settings.json", encoding='utf-8')
except (FileNotFoundError):
    print("Не удалось открыть файл начальных настроек! Проверитье его наличие!")
    exit(1)
json_data = json.load(file)
file.close()

print("Введите количество комнат (целое неотрицательное число)")
tmp_read = input()
while not( chek_int(tmp_read) ):
    print("Введите количество комнат (целое неотрицательное число)")
    tmp_read = input()
json_data["room"]["number"] = int(tmp_read)

for i in range(json_data["room"]["number"]):
    print("Введите ширину комнаты в метрах", i+1)
    tmp_read = input()
    while not (chek_float(tmp_read)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read = input()

    json_data["room"]["weight"].append(float(tmp_read))

    print("Введите длину комнаты в метрах", i + 1)
    tmp_read = input()
    while not (chek_float(tmp_read)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read = input()
    json_data["room"]["length"].append(float(tmp_read))

    print("Введите высоту комнаты в метрах", i + 1)
    tmp_read = input()
    while not (chek_float(tmp_read)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read = input()
    json_data["room"]["height"].append(float(tmp_read))

print("Введите время эмулирования в секундах")
tmp_read = input()
while not( chek_int(tmp_read) ):
    print("Ошибка ввода! Попробуйте еще раз!")
    tmp_read = input()
json_data["general"]["time_for_work"] = int(tmp_read)

print("Введите начальную температуру")
tmp_read = input()
while not (chek_float_temp(tmp_read)):
    print("Ошибка ввода! Попробуйте еще раз!")
    tmp_read = input()
json_data["climate"]["start_temperature"] = float(tmp_read)
print("Введите поддерживаемую температуру")
tmp_read = input()
while not (chek_float_temp(tmp_read)):
    print("Ошибка ввода! Попробуйте еще раз!")
    tmp_read = input()
json_data["climate"]["support_temperature"] = float(tmp_read)

print("Есть ли в доме кондиционер? (y/n)")
if input() == "y":
    print("Введите количесвто кондиционеров")
    tmp_read = input()
    while not (chek_int(tmp_read)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read = input()
    json_data["climate"]["conditioner"]["number"] = int(tmp_read)

    print("Введите мощность одного кондиционера")
    tmp_read = input()
    while not (chek_float(tmp_read)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read = input()
    json_data["climate"]["conditioner"]["power"] = float(tmp_read)

    print("Введите производтельность по холоду одного кондиционера")
    tmp_read = input()
    while not (chek_float(tmp_read)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read = input()
    json_data["climate"]["conditioner"]["frozen_power"] = float(tmp_read)
else:
    print("Окей, кондиционера нет")
    json_data["climate"]["conditioner"]["number"] = 0
    json_data["climate"]["conditioner"]["power"] = 0
    json_data["climate"]["conditioner"]["frozen_power"] = 0

print("Есть ли в доме обогреватель? (y/n)")
if input() == "y":
    print("Введите количесвто обогревателей")
    tmp_read = input()
    while not (chek_int(tmp_read)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read = input()
    json_data["climate"]["heater"]["number"] = int(tmp_read)

    print("Введите мощность одного обогревателя")
    tmp_read = input()
    while not (chek_float(tmp_read)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read = input()
    json_data["climate"]["heater"]["power"] = float(tmp_read)
else:
    print("Окей, обогревателей нет")
    json_data["climate"]["heater"]["number"] = 0
    json_data["climate"]["heater"]["power"] = 0


tmp_device = copy.deepcopy(json_data["device_templete"])

print("Есть ли в доме другие устройства? (y/n)")
if input() == "y":
    print("Сколько их?")
    tmp_read_1 = input()
    while not (chek_int(tmp_read_1)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read_1 = input()
    for i in range(int(tmp_read_1)):
        tmp_device = copy.deepcopy(json_data["device_templete"])
        print("Введите имя устройства")
        tmp_device["name"] = input()

        print("Введите мощность устройства")
        tmp_read = input()
        while not (chek_float(tmp_read)):
            print("Ошибка ввода! Попробуйте еще раз!")
            tmp_read = input()
        tmp_device["power"] = float(tmp_read)

        print("Введите количество запусков устройства")
        tmp_read = input()
        while not (chek_int(tmp_read)):
            print("Ошибка ввода! Попробуйте еще раз!")
            tmp_read = input()
        tmp_device["number_of_starts"] = int(tmp_read)

        for tmp_number in range(tmp_device["number_of_starts"]):
            print("Введите время включения", tmp_number+1)
            tmp_read = input()
            while not (chek_int_end_time(tmp_read)):
                print("Ошибка ввода! Попробуйте еще раз!")
                tmp_read = input()
            tmp_device["time_for_start"].append(int(tmp_read))
            print("Введите время выключения", tmp_number + 1)
            tmp_read = input()
            while not (chek_int_end_time(tmp_read)):
                print("Ошибка ввода! Попробуйте еще раз!")
                tmp_read = input()
            tmp_device["time_for_end"].append(int(tmp_read))
            tmp_device["spent_energy"]=0
        json_data["devices"].append(tmp_device)
        tmp_device = None

else:
    print("Окей, других устройств нет")

print("Нужно ли эмулировать открытие/закрытие форточек (y/n)")
if input() == "y":
    print("Введите количество открытий/закрытий форточек")
    tmp_read_2 = input()
    while not (chek_int(tmp_read_2)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read_2 = input()
    for i in range(int(tmp_read_2)):
        print("Введите время открытия форточки №", i)
        tmp_read = input()
        while not (chek_int_end_time(tmp_read)):
            print("Ошибка ввода! Попробуйте еще раз!")
            tmp_read = input()
        json_data["opening_window"]["time_for_open"].append(int(tmp_read))

        print("Введите время закрытия форточки №", i)
        tmp_read = input()
        while not (chek_int_end_time(tmp_read)):
            print("Ошибка ввода! Попробуйте еще раз!")
            tmp_read = input()
        json_data["opening_window"]["time_for_end"].append(int(tmp_read))

    print("Введите изменение температуры в секунду при открытии форточки")
    tmp_read = input()
    while not (chek_float_temp(tmp_read)):
        print("Ошибка ввода! Попробуйте еще раз!")
        tmp_read = input()
    json_data["opening_window"]["delta_temperature"] = float(tmp_read)
else:
    print("Ок. Эмулирования открытия форточек не будет")


with open('settings.json', 'w', encoding='utf-8 ') as file_for_write:
    file_for_write.write(json.dumps(json_data, indent=4))