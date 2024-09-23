from cProfile import label
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from translate import Translator
import os
import sys

# Отримать доступ до папки, де є файли
if getattr(sys, 'frozen', False):
    # якщо запущена як .exe
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

# Це base_path для доступу до зображень
image_path = os.path.join(base_path, 'img', 'src.png')

#Головне вікно
root=Tk()
root.title("Weather App | Погода ")
root.geometry("900x500+1100+40") #Тут =1100 і +40 це розміщення(пам'ятка)
root.resizable(False, False)

def getWeather():
    city = textfield.get()  # Отримуємо місто с вводу данних
    geolocator = Nominatim(user_agent="EsegyCode_weather_app")

    # Робимо об'єкт Translator для перекладу на англійський
    translator2 = Translator(to_lang="en")
    city_en = translator2.translate(city)

    # Знаходимо місцезнаходження
    location = geolocator.geocode(city_en)

    if location:
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude) #По кординатам шукає локацію

        #Час та надпис
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M")
        clock.config(text="     {}".format(current_time))
        name.config(text="ПОТОЧНА ПОГОДА")

        # Третя спроба нормально написать URL для API OpenWeatherMap
        api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=86e44870c51f3c1e84810cc34f209a05"

        # Отримання данних про погоду через АПІ
        json_data = requests.get(api).json()

        # Перевірка ключа 'weather' для отримання данних
        if 'weather' in json_data:
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'] - 273.15)  # Тут Кельвіни, тому віднімаю для отримання Цельсія
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            # Об'єкт типу транслятор для перекладу на українську
            translator = Translator(to_lang="uk")



            # Тут перевод тексту на українську
            condition_ua = translator.translate(condition)
            description_ua = translator.translate(description).capitalize()

            # Обновляєм значення в іньерфейсі через конфіг
            t.config(text=(temp, "°C"))
            c.config(text=condition_ua + " | Відчувається як " + str(temp) + "°C")
            w.config(text="{} м/c".format(wind))
            h.config(text="{}%".format(humidity))
            d.config(text=description_ua)
            p.config(text="{} гПА".format(pressure))
        else:
            print("Не вийшло отримати данні про погоду.")
    else:
        print("Не знайшло місцезнаходження. Перевірь правильність вхідних данних.")


#Коробка пошуку
Search_image = PhotoImage(file=os.path.join(base_path, 'img', 'src.png'))
myimage=Label(image=Search_image)
myimage.place(x=20, y=20)


#Ввід тексту
textfield=tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#606060", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()


# Прив'язка клавіші Enter до функції getWeather
textfield.bind("<Return>", lambda event: getWeather())

#Кнопка пошуку
Search_icon = PhotoImage(file=os.path.join(base_path, 'img', 'src_ic.png'))
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#606060", command=getWeather)
myimage_icon.place(x=400, y=34)

#Лого
Logo_image = PhotoImage(file=os.path.join(base_path, 'img', 'weather.png'))
mylogo=Label(image=Logo_image)
mylogo.place(x=150, y=120)

#Коробка під пошук
Frame_image = PhotoImage(file=os.path.join(base_path, 'img', 'box.png'))
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

#Час
name=Label(root, font=("arial", 15, "bold"))
name.place(x=15,y=110)
clock=Label(root,font=("Helvetica",20))
clock.place(x=15, y=140)

#label - Надписи для данних
label1=Label(root, text="ВІТЕР", font=("Helvetica", 15, 'bold'), fg="white", bg="#90baff")
label1.place(x=120, y=400)

label2=Label(root, text="ВОЛОГА", font=("Helvetica", 15, 'bold'), fg="white", bg="#90baff")
label2.place(x=250, y=400)

label3=Label(root, text="ОПИС", font=("Helvetica", 15, 'bold'), fg="white", bg="#90baff")
label3.place(x=400, y=400)

label4=Label(root, text="ТИСК", font=("Helvetica", 15, 'bold'), fg="white", bg="#90baff")
label4.place(x=650, y=400)

#t-температура, c - відчувається, w - вітер, h - вологість, d - опис, p - тиск
t=Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=420, y=150)
c=Label(font=("arial", 15, 'bold'))
c.place(x=450, y=250)
w=Label(text=" ...", font=("arial", 20, "bold"), bg="#90baff", fg="white")
w.place(x=120, y=430)
h=Label(text=" ...", font=("arial", 20, "bold"), bg="#90baff", fg="white")
h.place(x=260, y=430)
d=Label(text="   ...", font=("arial", 20, "bold"), bg="#90baff", fg="white")
d.place(x=390, y=430)
p=Label(text="   ...", font=("arial", 20, "bold"), bg="#90baff", fg="white")
p.place(x=640, y=430)

""" Не працює, потім добавлю (Обробіток підказки) - Не реагує та погано накладується
# Підказка для вводу Міста
hint_label = Label(root, text="Введи місто", font=("arial", 15), fg="black")
hint_label.place(x=50, y=10)

def on_entry_click(event):
    #Функція, визов при натисканні на текстове поле
    if textfield.get() == "":  # Якщо текстове поле порожнє
        textfield.delete(0, "end")  # Очищу текстове поле
        hint_label.place_forget()  # Сховати мою підказку

def on_focusout(event):
    #Функція, яка викликає втрачає фокус
    if textfield.get() == "":  # Поле зараз порожнє
        hint_label.place(x=50, y=10)  # Знову показати підказку (Нічого не получається)

# Додаємо обробники подій
textfield.bind("<FocusIn>", on_entry_click)
textfield.bind("<FocusOut>", on_focusout)

"""
print("Все працює чудово")

root.mainloop()


