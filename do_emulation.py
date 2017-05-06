import json


try:
    file = open("settings.json", encoding='utf-8')
except (FileNotFoundError):
    print("Не удалось открыть файл настроек! Проверитье его наличие!")
    exit(1)

json_data = json.load(file)
file.close()

current_temperature = json_data["climate"]["start_temperature"]
volume = 0
for i in range(json_data["room"]["number"]):
    volume += json_data["room"]["height"][i]*json_data["room"]["weight"][i]*json_data["room"]["length"][i]

mass = volume * 1.255

delta_temperature_of_heater = json_data["climate"]["heater"]["power"] * json_data["climate"]["heater"]["number"] / (1005*mass*3600)
delta_temperature_of_conditioner = json_data["climate"]["conditioner"]["frozen_power"] * json_data["climate"]["conditioner"]["number"] / (1005*mass*3600)

spent_energy = 0
spent_energy_by_conditioner = 0
spent_energy_by_heater = 0
current_state_of_climate = 1
log = []

for time_of_emulation in range(0, json_data["general"]["time_for_work"]):

    if current_state_of_climate == 1:
        current_temperature = current_temperature
    elif current_state_of_climate == 2:
        current_temperature -= delta_temperature_of_conditioner
        spent_energy += json_data["climate"]["conditioner"]["power"] * json_data["climate"]["conditioner"]["number"] / 3600
        spent_energy_by_conditioner += json_data["climate"]["conditioner"]["power"] * json_data["climate"]["conditioner"]["number"] / 3600
    elif current_state_of_climate == 3:
        current_temperature += delta_temperature_of_heater
        spent_energy += json_data["climate"]["heater"]["power"] * json_data["climate"]["heater"]["number"] / 3600
        spent_energy_by_heater += json_data["climate"]["heater"]["power"] * json_data["climate"]["heater"]["number"] / 3600

    for devices in json_data["devices"]:
        for number_of_interval in range(len(devices["time_for_start"])):
            if devices["time_for_start"][number_of_interval] <= time_of_emulation <= devices["time_for_end"][number_of_interval]:
                spent_energy+=devices["power"] / 3600
                devices["spent_energy"]+=devices["power"] / 3600

    for number_of_interval in range(len(json_data["opening_window"]["time_for_open"])):
        if json_data["opening_window"]["time_for_open"][number_of_interval] <= time_of_emulation <= json_data["opening_window"]["time_for_end"][number_of_interval]:
            current_temperature+=json_data["opening_window"]["delta_temperature"]

    log.append({
        "all_spent_energy": spent_energy,
        "time": time_of_emulation,
        "temperature" : current_temperature
    })

    if current_temperature == json_data["climate"]["support_temperature"]:
        current_state_of_climate = 1
    if current_temperature > json_data["climate"]["support_temperature"]:
        current_state_of_climate = 2
    if current_temperature < json_data["climate"]["support_temperature"]:
        current_state_of_climate = 3

spent_energy_by_each_device = {
    "name": [],
    "energy": []
}

for devices in json_data["devices"]:
    spent_energy_by_each_device["name"].append(devices["name"])
    spent_energy_by_each_device["energy"].append(devices["spent_energy"])

spent_energy_by_each_device["name"].append("Кондиционер")
spent_energy_by_each_device["energy"].append(spent_energy_by_conditioner)

spent_energy_by_each_device["name"].append("Обогреватель")
spent_energy_by_each_device["energy"].append(spent_energy_by_heater)

with open('log.json', 'w', encoding='utf-8') as file_for_write:
    file_for_write.write(json.dumps(log, indent=4))

with open('log_by_each_device.json', 'w', encoding='utf-8') as file_for_write:
    file_for_write.write(json.dumps(spent_energy_by_each_device, indent=4))

print("Эмулирование прошло успешно!")