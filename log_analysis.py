import matplotlib.pyplot as plt
import numpy as np
import json

file = open("log.json", encoding='utf-8')
json_data = json.load(file)
file.close()

yline = []
xline = []

for i in json_data:
    yline.append(i["all_spent_energy"])
    xline.append(i["time"])


radius = xline
area = yline
plt.plot(radius, area)
plt.xlabel('Прошло секунд со старта')
plt.ylabel('Потребленная энергия в Вт/ч')
plt.title('Общее потребление энергии')
plt.show()

#строим график температуры

yline = []
xline = []

for i in json_data:
    yline.append(i["temperature"])
    xline.append(i["time"])


radius = xline
area = yline
plt.plot(radius, area)
plt.xlabel('Прошло секунд со старта')
plt.ylabel('температура в цельсиях')
plt.title('Температура в каждый момент времени')
plt.show()

#построили

file = open("log_by_each_device.json", encoding='utf-8')
json_data = json.load(file)
file.close()

objects = []
performance = []

for number in range(len(json_data["name"])):
    performance.append(json_data["energy"][number])
    objects.append(json_data["name"][number])

y_pos = np.arange(len(objects))
plt.bar(y_pos, performance, align='center')
plt.xticks(y_pos, objects)
plt.ylabel('энергия в Вт/ч')
plt.title('Потребленная энергия каждым прибором')
plt.show()