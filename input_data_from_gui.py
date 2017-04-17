from tkinter import *
import json

file = open("default_settings.json", encoding='utf-8')
json_data = json.load(file)
file.close()


def result_room():

    json_data["room"]["number"] = int(ent_room_number.get(1.0, END))
    for item in range(json_data["room"]["number"]):
        json_data["room"]["height"].append(int(mas_ent_height[item].get(1.0, END)))
        json_data["room"]["weight"].append(int(mas_ent_weight[item].get(1.0, END)))
        json_data["room"]["length"].append(int(mas_ent_length[item].get(1.0, END)))

    rooms.destroy()
    lab_room_number.destroy()
    ent_room_number.destroy()
    but_room_number.destroy()

    lab_interval_of_time.pack()
    ent_interval_of_time.pack()
    lab_time_for_work.pack()
    ent_time_for_work.pack()
    lab_start_temperature.pack()
    ent_start_temperature.pack()
    lab_support_temperature.pack()
    ent_support_temperature.pack()
    lab_conditioner_number.pack()
    ent_conditioner_number.pack()
    lab_conditioner_power.pack()
    ent_conditioner_power.pack()
    lab_conditioner_power_frozen.pack()
    ent_conditioner_power_frozen.pack()
    lab_heater_number.pack()
    ent_heater_number.pack()
    lab_heater_power.pack()
    ent_heater_power.pack()
    but_all_ent.pack()


def room():
    global rooms
    rooms = Toplevel()
    for i in range(int(ent_room_number.get(1.0, END))):
        mas_label_height.append( Label(rooms, text="Введите высоту конматы:" + str(i+1) , font="Arial 14") )
        mas_ent_height.append(Text(rooms, width=20, bd=0, height=1, font="Arial 14"))
        mas_label_weight.append( Label(rooms, text="Введите ширину комнаты:" + str(i+1) , font="Arial 14") )
        mas_ent_weight.append(Text(rooms, width=20, bd=0, height=1, font="Arial 14"))
        mas_label_length.append( Label(rooms, text="Введите длину комнаты:" + str(i+1) , font="Arial 14"))
        mas_ent_length.append(Text(rooms, width=20, bd=0, height=1, font="Arial 14"))

    for i in range(int(ent_room_number.get(1.0, END))):
        mas_label_height[i].pack()
        mas_ent_height[i].pack()
        mas_label_weight[i].pack()
        mas_ent_weight[i].pack()
        mas_label_length[i].pack()
        mas_ent_length[i].pack()

    Button(rooms, text="Внести значения в файл настроек и продолжить",
          width=40, height=2,
          bg="white",fg="black", font="Arial 10", command = result_room).pack()


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))


def all_general():
    json_data["general"]["interval_of_time"] = int(ent_interval_of_time.get(1.0, END))
    json_data["general"]["time_for_work"] = int(ent_time_for_work.get(1.0, END))
    json_data["climate"]["start_temperature"] = int(ent_start_temperature.get(1.0, END))
    json_data["climate"]["support_temperature"] = int(ent_support_temperature.get(1.0, END))
    json_data["climate"]["heater"]["number"] = int(ent_heater_number.get(1.0, END))
    json_data["climate"]["heater"]["power"] = int(ent_heater_power.get(1.0, END))
    json_data["climate"]["conditioner"]["number"] = int(ent_conditioner_number.get(1.0, END))
    json_data["climate"]["conditioner"]["power"] = int(ent_conditioner_power.get(1.0, END))
    json_data["climate"]["conditioner"]["frozen_power"] = int(ent_conditioner_power_frozen.get(1.0, END))

    with open('settings.json', 'w', encoding='utf-8 ') as file_for_write:
        file_for_write.write(json.dumps(json_data, indent=4))

    lab_interval_of_time.destroy()
    ent_interval_of_time.destroy()
    lab_time_for_work.destroy()
    ent_time_for_work.destroy()
    lab_start_temperature.destroy()
    ent_start_temperature.destroy()
    lab_support_temperature.destroy()
    ent_support_temperature.destroy()
    lab_conditioner_number.destroy()
    ent_conditioner_number.destroy()
    lab_conditioner_power.destroy()
    ent_conditioner_power.destroy()
    lab_conditioner_power_frozen.destroy()
    ent_conditioner_power_frozen.destroy()
    lab_heater_number.destroy()
    ent_heater_number.destroy()
    lab_heater_power.destroy()
    ent_heater_power.destroy()
    but_all_ent.destroy()
    root.destroy()


root = Tk()

root.title('SH')

# --- create canvas with scrollbar ---

canvas = Canvas(root,width=900,height=1000)

canvas.pack(side=LEFT)

scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# --- add widgets in frame ---

mas_label_height = []
mas_label_weight = []
mas_label_length = []

mas_ent_height = []
mas_ent_weight = []
mas_ent_length = []

lab_room_number = Label(frame, text="Введите количество комнат",  font="Arial 14")
ent_room_number = Text(frame, width=20,bd=0,height=1, font="Arial 14")
but_room_number = Button(frame,
          text="Ввести значения для каждой комнаты",
          width=40, height=2,
          bg="white",fg="black", font="Arial 10", command = room)

lab_interval_of_time = Label(frame, text="Введите время между считыванием данных",  font="Arial 14")
ent_interval_of_time = Text(frame, width=20,bd=0,height=1, font="Arial 14")

lab_time_for_work = Label(frame, text="Введите время эмулирования",  font="Arial 14")
ent_time_for_work = Text(frame, width=20,bd=0,height=1, font="Arial 14")

lab_start_temperature = Label(frame, text="Введите начальную температуру",  font="Arial 14")
ent_start_temperature = Text(frame, width=20,bd=0,height=1, font="Arial 14")

lab_support_temperature = Label(frame, text="Введите поддерживаемую температуру",  font="Arial 14")
ent_support_temperature = Text(frame, width=20,bd=0,height=1, font="Arial 14")

lab_conditioner_number = Label(frame, text="Введите количество кондиционеров",  font="Arial 14")
ent_conditioner_number = Text(frame, width=20,bd=0,height=1, font="Arial 14")

lab_conditioner_power = Label(frame, text="Введите потребляемую мощность кондиционера",  font="Arial 14")
ent_conditioner_power = Text(frame, width=20,bd=0,height=1, font="Arial 14")

lab_conditioner_power_frozen = Label(frame, text="Введите мощность кондиционера по холоду",  font="Arial 14")
ent_conditioner_power_frozen = Text(frame, width=20,bd=0,height=1, font="Arial 14")

lab_heater_number = Label(frame, text="Введите количество обогревателей",  font="Arial 14")
ent_heater_number = Text(frame, width=20,bd=0,height=1, font="Arial 14")

lab_heater_power = Label(frame, text="Введите потребляемую мощность обогревателя",  font="Arial 14")
ent_heater_power = Text(frame, width=20,bd=0,height=1, font="Arial 14")

but_all_ent = Button(frame,
          text="Внести значения в файл настроек и продолжить",
          width=40, height=2,
          bg="white",fg="black", font="Arial 10", command = all_general)

lab_room_number.pack()
ent_room_number.pack()
but_room_number.pack()


# --- start program ---

root.mainloop()