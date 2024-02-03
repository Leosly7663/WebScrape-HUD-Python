import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import datetime
from WebScrape import scrapeCity, scrapeWeather

# Initialize default values
currentWeather = "Cloudy"
currentTime = "12:00"
currentTemp = "12°C"
currentFeel = "15°C"
currentWind = "12km/h NE"
currentHumidity = "50%"
currentDewpoint = "0°C"
currentPressure = "1000mbar"
currentPrecipitation = "10mm"
currentVisibility = "15km"
forcastTime = "null"
conditionsForcast = "null"
temperatureAndFeelsLikeForcast = "null"
otherStuffForcastA = "null"
otherStuffForcastB = "null"
otherStuffForcastC = "null"
otherStuffForcastD = "null"
otherStuffForcastE = "null"
otherStuffForcastF = "null"

# Create main window
window = tk.Tk()
window.title("Weather")
window.geometry("800x600")  # Set your preferred window size

# Define fonts
fontStyle = tkFont.Font(family="Times New Roman", size=25)
fontStyleSmall = tkFont.Font(family="Times New Roman", size=10)
fontStyleBig = tkFont.Font(family="Times New Roman", size=70)

# Create frames
topFrame = Frame(window, bg="lightgray")
leftFrame = Frame(window, bg="lightgray")
rightFrame = Frame(window, bg="lightgray")

# Define labels
leftLabel = Label(leftFrame, text="Current Conditions:", font=fontStyle, bg="lightgray")
temperatureCurrent = Label(leftFrame, text=currentTemp, font=fontStyleBig, bg="lightgray")
feelsLikeCurrent = Label(leftFrame, text=currentFeel, font=fontStyle, bg="lightgray")
humidityCurrent = Label(leftFrame, text=currentHumidity, font=fontStyle, bg="lightgray")
windSpeedCurrent = Label(leftFrame, text=currentWind, font=fontStyle, bg="lightgray")
dewpointCurrent = Label(leftFrame, text=currentDewpoint, font=fontStyle, bg="lightgray")
pressureCurrent = Label(leftFrame, text=currentPressure, font=fontStyle, bg="lightgray")
precipitationCurrent = Label(leftFrame, text=currentPrecipitation, font=fontStyle, bg="lightgray")
visibilityCurrent = Label(leftFrame, text=currentVisibility, font=fontStyle, bg="lightgray")

# Place labels
leftLabel.grid(row=0, sticky=W, pady=10)
temperatureCurrent.grid(row=1, sticky=W, pady=10)
feelsLikeCurrent.grid(row=2, sticky=W, pady=10)
humidityCurrent.grid(row=3, sticky=W, pady=10)
windSpeedCurrent.grid(row=4, sticky=W, pady=10)
dewpointCurrent.grid(row=5, sticky=W, pady=10)
pressureCurrent.grid(row=6, sticky=W, pady=10)
precipitationCurrent.grid(row=7, sticky=W, pady=10)
visibilityCurrent.grid(row=8, sticky=W, pady=10)

# Place frames
topFrame.pack(side=TOP, fill=X)
leftFrame.pack(side=LEFT, padx=20, pady=20)
rightFrame.pack(side=RIGHT, padx=20, pady=20)

# Create menu
menu_bar = Menu(topFrame)
settings_menu = Menu(menu_bar, tearoff=0)

def option_selected(name):
    print(name)
    print(names.index(name))
    print(links[names.index(name)])
    link = links[names.index(name)]
    scrapeWeather(link)


# Define dropdown menu
dropdown_menu = Menu(settings_menu, tearoff=0)
names = []
links = []
scrapeCity(names, links) 


for index, option in enumerate(names, start=1):
    settings_menu.add_command(label=option, command=lambda opt=option: option_selected(opt))


# Add dropdown menu to Settings menu
settings_menu.add_cascade(label="Dropdown Option", menu=dropdown_menu)


# Add Settings menu to the menu bar
menu_bar.add_cascade(label="City", menu=settings_menu)

# Attach menu to window
window.config(menu=menu_bar)

# Start the GUI event loop
window.mainloop()
