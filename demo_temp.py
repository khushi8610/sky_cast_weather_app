from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e440e57456d1b834ea5208f0b27d726b"
        data = requests.get(url).json()
        print(data)
        W_label1.config(text=data["weather"][0]["main"])
        Wb_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)) + " °C")
        per_label1.config(text=str(data["main"]["pressure"]) + " hPa")

win = Tk()
win.title("SkyCast Weather App")
win.config(bg="blue")
win.geometry("500x570")

city_name = StringVar()

name_label = Label(win, text="SkyCast Weather App",
                   font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

com = ttk.Combobox(win, values=list_name,
                   font=("Times New Roman", 20, "bold"),
                   textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

W_label = Label(win, text="Weather Climate", font=("Times New Roman", 20,))
W_label.place(x=25, y=260, height=40, width=210)

W_label1 = Label(win, text="", font=("Times New Roman", 20))
W_label1.place(x=250, y=260, height=40, width=210)

Wb_label = Label(win, text="Description", font=("Times New Roman", 17,))
Wb_label.place(x=25, y=310, height=40, width=210)

Wb_label1 = Label(win, text="", font=("Times New Roman", 17))
Wb_label1.place(x=250, y=310, height=40, width=210)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 20,))
temp_label.place(x=25, y=360, height=40, width=210)

temp_label1 = Label(win, text="", font=("Times New Roman", 20))
temp_label1.place(x=250, y=360, height=40, width=210)

per_label = Label(win, text="Pressure", font=("Times New Roman", 20,))
per_label.place(x=25, y=410, height=40, width=210)

per_label1 = Label(win, text="", font=("Times New Roman", 20))
per_label1.place(x=250, y=410, height=40, width=210)

done_button = Button(win, text="Done", font=("Times New Roman", 20, "bold"), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()
