import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import datetime
from WebScrape import scrapeCity, scrapeWeather

# Initialize default values


"""
Heres a raw data sample 
['Observed at:', 'Saint-Anicet', '11:00 PM', 'EST', 'Condition:', 'Not observed', 'Pressure:', '101.7', 'kPa', 'Tendency:', 'Falling', 'Temperature:', '-7.0°', 'C', 'Dew point:', '-7.5°', 'C', 'Humidity:', '96%', 'Wind:', 'calm', '-7°', 'C', 'Condition:', 'Not observed', 'Pressure:', '101.7', 'kPa']
[['Tonight', '-14', '°', 'C', 'Partly cloudy'], 
['Mon', '5', 'Feb', '-1', '°', 'C', 'A mix of sun and cloud', 'Night', '-16', '°', 'C', 'A few clouds'], 
['Tue', '6', 'Feb', '-3', '°', 'C', 'Sunny', 'Night', '-11', '°', 'C', 'Clear'],
['Wed', '7', 'Feb', '-1', '°', 'C', 'Sunny', 'Night', '-8', '°', 'C', 'Clear'],
['Thu', '8', 'Feb', '3', '°', 'C', 'A mix of sun and cloud', 'Night', '-3', '°', 'C', 'Cloudy'],
['Fri', '9', 'Feb', '5', '°', 'C', 'Cloudy', 'Night', '3', '°', 'C', '60%', 'Chance of showers'],
['Sat', '10', 'Feb', '6', '°', 'C', '60%', 'Chance of showers']]
"""


observedAt = "Saint-Anicet 11:00 PM EST"
condition = "Not Observed"
pressure = "101.7 kPa"
tendency = "Falling"
temperature = "-7°C"
dewPoint = "-7.5°C"
humdity = "96%"
wind = "calm" 

# Create main window
window = tk.Tk()
window.title("Weather")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.minsize(width=screen_width, height=screen_height)
window.resizable(width=True, height=True)


# Define fonts
fontStyle = tkFont.Font(family="Times New Roman", size=25)
fontStyleSmall = tkFont.Font(family="Times New Roman", size=10)
fontStyleBig = tkFont.Font(family="Times New Roman", size=70)

# Create frames
topFrame = Frame(window, bg="lightgray")
leftFrame = Frame(window, bg="lightgray")
rightFrame = Frame(window, bg="white")


# Define labels
leftLabel = Label           (leftFrame, text="Current Conditions:", font=fontStyle, bg="lightgray").grid        (row=0, sticky=W, pady=10)
temperatureCurrent = Label  (leftFrame, text=temperature, font=fontStyleBig, bg="lightgray").grid               (row=1, sticky=W, pady=10)
conditionCurrent = Label    (leftFrame, text=condition, font=fontStyleBig, bg="lightgray").grid                 (row=2, sticky=W, pady=10)
tendencyCurrent = Label     (leftFrame, text="Tendency: "+tendency, font=fontStyle, bg="lightgray").grid        (row=3, sticky=W, pady=10)
humidityCurrent = Label     (leftFrame, text="Humidity: "+humdity, font=fontStyle, bg="lightgray").grid         (row=4, sticky=W, pady=10)
windSpeedCurrent = Label    (leftFrame, text="Wind: "+wind, font=fontStyle, bg="lightgray").grid                (row=5, sticky=W, pady=10)
dewpointCurrent = Label     (leftFrame, text="Dewpoint: "+dewPoint, font=fontStyle, bg="lightgray").grid        (row=6, sticky=W, pady=10)
pressureCurrent = Label     (leftFrame, text="Pressure: "+pressure, font=fontStyle, bg="lightgray").grid        (row=7, sticky=W, pady=10)
observedAtCurrent = Label   (leftFrame, text="Observed at: "+observedAt, font=fontStyle, bg="lightgray").grid   (row=8, sticky=W, pady=10)


# [['Tonight', '-14', '°', 'C', 'Partly cloudy'], 
def tonightLabel():
        
        day = Label  (rightFrame, text="Tonight", font=fontStyle, bg="lightgray").grid      (row=1, sticky=W, pady=10)
        blank = Label  (rightFrame, bg="white").grid                                            (row=2, sticky=W, pady=5, )
        conditions = Label  (rightFrame, text="Partly cloudy", font=fontStyle, bg="lightgray").grid      (row=3, sticky=W)
        gif = Label  (rightFrame, text="-14°C", font=fontStyle, bg="lightgray").grid      (row=4,column=1, sticky=W)
        temp = Label  (rightFrame, text="-14°C", font=fontStyle, bg="lightgray").grid      (row=4, column=2, sticky=W)

tonightLabel()

# ['Mon', '5', 'Feb', '-1', '°', 'C', 'A mix of sun and cloud', 'Night', '-16', '°', 'C', 'A few clouds'], 
def tonightLabel():
        
        day = Label  (rightFrame, text="Mon 5 Feb", font=fontStyle, bg="lightgray").grid      (row=1, sticky=W, pady=10)
        blank = Label  (rightFrame, bg="white").grid                                            (row=2, sticky=W, pady=5, )
        conditions = Label  (rightFrame, text="'A mix of sun and cloud", font=fontStyle, bg="lightgray").grid      (row=3, sticky=W)
        gif = Label  (rightFrame, text="-14°C", font=fontStyle, bg="lightgray").grid      (row=4,column=1, sticky=W)
        temp = Label  (rightFrame, text="-14°C", font=fontStyle, bg="lightgray").grid      (row=4, column=2, sticky=W)

tonightLabel()


# Place frames
topFrame.pack(side=TOP, fill=X)
leftFrame.pack(side=LEFT, padx=20, pady=20)
rightFrame.pack(side=RIGHT,  pady=20)

# Create menu
menu_bar = Menu(topFrame)
settings_menu = Menu(menu_bar, tearoff=0)


# turns image names and size coordinates into usable photoimages
def makeImage(image,x,y):
    image1 = Image.open(image+".png")
    test = ImageTk.PhotoImage(image1.resize((x, y)))
    return test

def option_selected(name):
    mainForecast = []
    forecastGifs = []
    futureForecast = [[],[],[],[],[],[],[]]
    link = links[names.index(name)]
    scrapeWeather(link, mainForecast, futureForecast, forecastGifs)


# Define dropdown menu
dropdown_menu = Menu(settings_menu, tearoff=0)
names = []
links = []
scrapeCity(names, links) 


for index, option in enumerate(names, start=1):
    settings_menu.add_command(label=option, command=lambda opt=option: option_selected(opt))

fontStyle3 = tkFont.Font(family="Times New Roman", size=35)
fontStyle4 = tkFont.Font(family="Times New Roman", size=30)
color = "black"

date = datetime.datetime.now()
date = date.strftime("%x")
now = date

timeDisplay = Label(rightFrame, bg="lightgray", text=now, font=fontStyle3,fg=color)
timeDisplay.grid(row=12,sticky=E)
dateDisplay = Label(rightFrame, bg="lightgray", text=date, font=fontStyle4,fg=color)
dateDisplay.grid(row=11,pady=(335,0),sticky=E)



def play():
    global now, timeDisplay
    x = datetime.datetime.now()
    now = (x.strftime("%X"))
    timeDisplay.grid_forget()
    timeDisplay = Label(rightFrame, bg="lightgray", text=now, font=fontStyle3)
    timeDisplay.grid(row=12,stick=E)
    rightFrame.after(200, play)
play()

# Add dropdown menu to Settings menu
settings_menu.add_cascade(label="Dropdown Option", menu=dropdown_menu)


# Add Settings menu to the menu bar
menu_bar.add_cascade(label="City", menu=settings_menu)

# Attach menu to window
window.config(menu=menu_bar)

# Start the GUI event loop
window.mainloop()
