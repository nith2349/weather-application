from tkinter import *
import requests
import os
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
    additionalinfo = "\n" + "Feels like :" + str(feelslike) + "C" + "\n" + "Lowest :" + str(lowest) + "C" + "\n" + "Highest :" + str(highest) + "C" +"\n" + "Pressure :" + str(pressure) + "\n" + "Humidity :" + str(humidity) + "\n" + "Wind Speed :" + str(windspeed) + "\n" + "Visibility :" + str(visibility) 

    #display data
    data1.config(text=maindata)
    data2.config(text=additionalinfo)


#init Tkinter
weatherapp = Tk()
weatherapp.title("Weather App")
weatherapp.geometry("720x1280")
weatherapp.configure(bg = "white")

#Font
font1 = ("times",20,"bold")
font2 = ("times",45,"bold")

#Label
data1 = Label(weatherapp, font = font2)
data2 = Label(weatherapp, font = font1)

#entry box
dataentry = Entry(weatherapp, justify='center', width=30,font=data2)
dataentry.focus()
dataentry.bind('<Return>', openweatherdata)

checkbutton =  Button(weatherapp, text ="check",command = openweatherdata)

# Building Interface
dataentry.pack(pady=35)
data1.pack()
data2.pack()
checkbutton.pack(pady=45)

weatherapp.mainloop()