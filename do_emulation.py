import json

file = open("settings.json", encoding='utf-8')
json_data = json.load(file)
file.close()

current_temperature = json_data["climate"]["start_temperature"]
volume = 0
for i in range(json_data["room"]["number"]):
    volume += json_data["room"]["height"][i]*json_data["room"]["weight"][i]*json_data["room"]["length"][i]

mass = volume * 1.255

delta_temperature_of_heater = json_data["climate"]["heater"]["power"] * json_data["climate"]["heater"]["number"] / (1005*mass)
delta_temperature_of_conditioner = json_data["climate"]["conditioner"]["frozen_power"] * json_data["climate"]["conditioner"]["number"] / (1005*mass)
delta_spent_energy_of_other_device = 0
for number in range(len(json_data["devices"]["name"])):
    delta_spent_energy_of_other_device += json_data["devices"]["power"][number] * json_data["devices"]["operating_time"][number] * 0.00028 / json_data["general"]["time_for_work"]

spent_energy = 0
spent_energy_by_conditioner = 0
spent_energy_by_heater = 0
current_state_of_climate = 1
log = []

for time_of_emulation in range(0,json_data["general"]["time_for_work"],json_data["general"]["interval_of_time"]):

    if current_state_of_climate == 1:
        current_temperature = current_temperature
    elif current_state_of_climate == 2:
        current_temperature -= delta_temperature_of_conditioner
        spent_energy += json_data["climate"]["conditioner"]["power"] * json_data["general"]["interval_of_time"] * 0.00028 * json_data["climate"]["conditioner"]["number"]
        spent_energy_by_conditioner += json_data["climate"]["conditioner"]["power"] * json_data["general"]["interval_of_time"] * 0.00028 * json_data["climate"]["conditioner"]["number"]
    elif current_state_of_climate == 3:
        current_temperature += delta_temperature_of_heater
        spent_energy += json_data["climate"]["heater"]["power"] * json_data["general"]["interval_of_time"] * 0.00028 * json_data["climate"]["heater"]["number"]
        spent_energy_by_heater += json_data["climate"]["heater"]["power"] * json_data["general"]["interval_of_time"] * 0.00028 * json_data["climate"]["heater"]["number"]

    spent_energy += delta_spent_energy_of_other_device

    log.append({
        "all_spent_energy": spent_energy,
        "time": time_of_emulation,
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

    for number in range(len(json_data["devices"]["name"])):
        spent_energy_by_each_device["name"].append(json_data["devices"]["name"][number])
        spent_energy_by_each_device["energy"].append(json_data["devices"]["power"][number] * json_data["devices"]["operating_time"][number] * 0.00028)

    spent_energy_by_each_device["name"].append("Кондиционер")
    spent_energy_by_each_device["energy"].append(spent_energy_by_conditioner)

    spent_energy_by_each_device["name"].append("Обогреватель")
    spent_energy_by_each_device["energy"].append(spent_energy_by_heater)

with open('log.json', 'w', encoding='utf-8') as file_for_write:
    file_for_write.write(json.dumps(log, indent=4))


with open('log_by_each_device.json', 'w', encoding='utf-8') as file_for_write:
    file_for_write.write(json.dumps(spent_energy_by_each_device, indent=4))