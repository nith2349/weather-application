from tkinter import *
import requests
import os
from PIL import Image, ImageTk
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("apikey")

def openweatherdata():
    citiesdata = dataentry.get()
    apilink = "https://api.openweathermap.org/data/2.5/weather?q=" + citiesdata + "&appid=" + apikey
    #K to C
    ktoc = 273.2
    json = requests.get(apilink).json()
    apidata = json['weather'][0]['main']
    temparature = int(json['main']['temp']-ktoc)
    feelslike = int(json['main']['feels_like']-ktoc)
    lowest = int(json['main']['temp_min']-ktoc)
    highest = int(json['main']['temp_max']-ktoc)
    pressure = json['main']['pressure']
    humidity = json['main']['humidity']
    visibility = json['visibility']
    windspeed = json['wind']['speed']

    maindata = apidata + "\n" + str(temparature) + "C"
    additionalinfo = "\n" + "Feels like: " + str(feelslike) + "C" + "\n" + "Lowest: " + str(lowest) + "C" + "\n" + "Highest: " + str(highest) + "C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(windspeed) + "\n" + "Visibility: " + str(visibility)

    #Display data
    data1.config(text=maindata)
    data2.config(text=additionalinfo)

    #Load weather icon
    icon_id = json['weather'][0]['icon']
    icon_url = "https://openweathermap.org/img/w/" + icon_id + ".png"
    response = requests.get(icon_url, stream=True)
    if response.status_code == 200:
        with open("weather_icon.png", 'wb') as file:
            file.write(response.content)
        weather_icon = Image.open("weather_icon.png")
        weather_icon = weather_icon.resize((100, 100), Image.ANTIALIAS)
        weather_icon = ImageTk.PhotoImage(weather_icon)
        icon_label.config(image=weather_icon)
        icon_label.image = weather_icon

#Tkinter
weatherapp = Tk()
weatherapp.title("Weather App")
weatherapp.geometry("720x1280")
weatherapp.configure(bg="#F0F0F0")

#Frame for input and button
frame_input = Frame(weatherapp, bg="#F0F0F0")
frame_input.pack(pady=50)

#Label and entry box
label_city = Label(frame_input, text="Enter City Name:", font=("Times", 20), bg="#F0F0F0")
label_city.pack(side=LEFT, padx=10)
dataentry = Entry(frame_input, justify='center', width=30, font=("Times", 20))
dataentry.focus()
dataentry.pack(side=LEFT, padx=10)

#Button
checkbutton = Button(frame_input, text="Check", command=openweatherdata, font=("Times", 20))
checkbutton.pack(side=LEFT, padx=10)

#Frame for weather data
frame_weather = Frame(weatherapp, bg="#F0F0F0")
frame_weather.pack(pady=50)

#Weather icon label
icon_label = Label(frame_weather, bg="#F0F0F0")
icon_label.pack()

#Labels to display weather data
data1 = Label(frame_weather, font=("Times", 45, "bold"), bg="#F0F0F0")
data1.pack()
data2 = Label(frame_weather, font=("Times", 20), bg="#F0F0F0")
data2.pack()

weatherapp.mainloop()