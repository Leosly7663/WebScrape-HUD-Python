import tkinter as tk
import re
from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import datetime
from WebScrape import scrapeCity, scrapeWeather

# Initialize default values
color = "white"
bgColor = "lightgray"
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


observedAt = "Saint-Anicet 11:00 PM EST" # [1]+[2]+[3]
condition = "Not Observed" #[5]
pressure = "101.7 kPa" # [7] + [8]
tendency = "Falling" # [10]
temperature = "-7°C" # [12] + [13]
dewPoint = "-7.5°C" # [15] + [16]
humdity = "96%" # [18]
wind = "calm" # [20]



# Create main window
window = tk.Tk()
window.title("Weather")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.minsize(width=screen_width, height=screen_height)
window.resizable(width=True, height=True)
window.configure(background=bgColor)

window.attributes("-transparentcolor", "lightgray")
window.attributes("-topmost", True)

# Define fonts
fontStyle = tkFont.Font(family="Times New Roman", size=25)
fontStyleSmall = tkFont.Font(family="Times New Roman", size=10)
fontStyleBig = tkFont.Font(family="Times New Roman", size=70)

# Create frames
topFrame = Frame(window, bg="lightgray")
leftFrame = Frame(window, bg="lightgray")
rightFrame = Frame(window, bg="lightgray")

names = []
links = []
scrapeCity(names, links) 

# turns image names and size coordinates into usable photoimages
def makeImage(image,x,y):
    image1 = Image.open("temp/"+image+".gif")
    test = ImageTk.PhotoImage(image1.resize((x, y)))
    return test

mainForecast = []
futureForecast = [[],[],[],[],[],[],[]]

def option_selected(name, mainForecast, futureForecast):
    forecastGifs = []
    link = links[names.index(name)]
    scrapeWeather(link, mainForecast, futureForecast, forecastGifs)
    
option_selected("Barrie", mainForecast, futureForecast) # default city for startup is my home town Barrie ON <3

# this should work but we need to rescrape and repack every 3 mins TODO
observedAt = mainForecast[1]+" "+mainForecast[2]+" "+mainForecast[3]
condition = mainForecast[5]
pressure = mainForecast[7] + mainForecast[8]
tendency = mainForecast[10]
temperature = mainForecast[12] + mainForecast[13]
dewPoint = mainForecast[15] + mainForecast[16]
humdity = mainForecast[18]
wind = mainForecast[20]


# Define labels
leftLabel = Label           (leftFrame, text="Current Conditions:", font=fontStyle, bg="lightgray",fg=color).grid        (row=0, sticky=E, pady=10)
temperatureCurrent = Label  (leftFrame, text=temperature, font=fontStyleBig, bg="lightgray",fg=color).grid               (row=1, sticky=E, pady=10)
conditionCurrent = Label    (leftFrame, text=condition, font=fontStyleBig, bg="lightgray",fg=color).grid                 (row=2, sticky=E, pady=10)
tendencyCurrent = Label     (leftFrame, text="Tendency: "+tendency, font=fontStyle, bg="lightgray",fg=color).grid        (row=3, sticky=E, pady=10)
humidityCurrent = Label     (leftFrame, text="Humidity: "+humdity, font=fontStyle, bg="lightgray",fg=color).grid         (row=4, sticky=E, pady=10)
windSpeedCurrent = Label    (leftFrame, text="Wind: "+wind, font=fontStyle, bg="lightgray",fg=color).grid                (row=5, sticky=E, pady=10)
dewpointCurrent = Label     (leftFrame, text="Dewpoint: "+dewPoint, font=fontStyle, bg="lightgray",fg=color).grid        (row=6, sticky=E, pady=10)
pressureCurrent = Label     (leftFrame, text="Pressure: "+pressure, font=fontStyle, bg="lightgray",fg=color).grid        (row=7, sticky=E, pady=10)
observedAtCurrent = Label   (leftFrame, text="Observed at: "+observedAt, font=fontStyle, bg="lightgray",fg=color).grid   (row=8, sticky=E, pady=10)

def dayLabel(i, temp, conditions, night):
        offset = 0
        if night: offset = 1
        test = makeImage(str(i),32,32)
        conditions = Label  (rightFrame, text=conditions, font=fontStyle, bg="lightgray",fg=color).grid      (row=2*i+offset,column=3, sticky=W)
        labelImage = Label  (rightFrame, image=test )
        labelImage.image = test
        labelImage.grid      (row=i+(6*offset),column=1, sticky=W)
        temp = Label  (rightFrame, text=temp, font=fontStyle, bg="lightgray",fg=color).grid      (row=2*i+offset,column=2, sticky=E)


# [['Tonight', '-14', '°', 'C', 'Partly cloudy'], 

# have to secure my job security so comments? no <3
tonightText = futureForecast[0][0]
if tonightText == "Tonight":
    day = Label  (rightFrame, text=tonightText, font=fontStyle, bg="lightgray",fg=color).grid      (row=1, sticky=W, )
    dayLabel(0, futureForecast[0][1] + futureForecast[0][2]+ futureForecast[0][3], futureForecast[0][4])
else:
     for i in range(0,6):
          j =0
          tonightText = futureForecast[i][0] + futureForecast[i][1] + futureForecast[i][2]
          day = Label  (rightFrame, text=tonightText, font=fontStyle, bg="lightgray",fg=color).grid      (row=2*i,column=0, sticky=W, )

          if re.search(r"%$",futureForecast[i][6]):
               j = 1
               conditionsPassed = futureForecast[i][6] + futureForecast[i][7]
               tempPassedNext = futureForecast[i][9] + futureForecast[i][10]+ futureForecast[i][11]
          else:
               conditionsPassed = futureForecast[i][6]
               tempPassedNext = futureForecast[i][8] + futureForecast[i][9]+ futureForecast[i][10]

          dayLabel(i, futureForecast[i][3] + futureForecast[i][4] + futureForecast[i][5], conditionsPassed, False)
          night = Label  (rightFrame, text="Night", font=fontStyle, bg="lightgray",fg=color).grid      (row=2*i+1,column=0, sticky=W, )

          if re.search(r"%$",futureForecast[i][10]):
               conditionsPassed = futureForecast[i][11+j] + futureForecast[i][12+j]
          else:
               conditionsPassed = futureForecast[i][11+j]
          dayLabel(i, tempPassedNext, conditionsPassed, True)

""" 
[['Mon', '19', 'Feb', '-4', '°', 'C', 'A few flurries', 'Tonight', '-15', '°', 'C', 'Mainly cloudy'], 
['Tue', '20', 'Feb', '1', '°', 'C', 'Sunny', 'Night', '-4', '°', 'C', 'Cloudy periods'], 
['Wed', '21', 'Feb', '4', '°', 'C', '30%', 'Chance of showers', 'Night', '0', '°', 'C', '60%', 'Chance of rain showers or flurries'],
['Thu', '22', 'Feb', '4', '°', 'C', '40%', 'Chance of flurries or rain showers', 'Night', '-5', '°', 'C', '40%', 'Chance of flurries'], 
['Fri', '23', 'Feb', '-2', '°', 'C', '40%', 'Chance of flurries', 'Night', '-11', '°', 'C', '30%', 'Chance of flurries'], 
['Sat', '24', 'Feb', '-4', '°', 'C', '40%', 'Chance of flurries', 'Night', '-8', '°', 'C', '30%', 'Chance of flurries'], 
['Sun', '25', 'Feb', '1', '°', 'C', '30%', 'Chance of flurries']]
"""


# Place frames
topFrame.pack(side=TOP, fill=BOTH)

rightFrame.pack(side=LEFT,  pady=20, fill=Y)

leftFrame.pack(side=RIGHT, padx=20, pady=20)

# Create menu
menu_bar = Menu(topFrame)
cities_menu = Menu(menu_bar, tearoff=0)
settings_menu = Menu(menu_bar, tearoff=0)


# Define dropdown menu
dropdown_menu = Menu(cities_menu, tearoff=0)
bgColor_menu = Menu(settings_menu, tearoff=0)

# call me evil for this
# alright I know its illegal, BUT IM DUMB
global onTop
onTop = True

global transTog
transTog = True



def handleStayOnTop():
    global onTop
    onTop = not onTop
    window.attributes("-topmost", onTop)

def handleTransparency():
    global transTog
    transTog = not transTog
    window.configure(background='lightgray')
    rightFrame.configure(background='lightgray')
    topFrame.configure(background='lightgray')
    leftFrame.configure(background='lightgray')
    if transTog:
        window.attributes("-transparentcolor", "lightgray")
    else:
         window.attributes("-transparentcolor", "purple")

def handleBgChange(opt):
    window.configure(background=opt)
    rightFrame.configure(background=opt)
    topFrame.configure(background=opt)
    leftFrame.configure(background=opt)


     
settings_menu.add_command(label="Stay on top", command=lambda : handleStayOnTop())
settings_menu.add_command(label="Transparency", command=lambda : handleTransparency())

bgColor_menu.add_command(label="Black", command=lambda opt="Black": handleBgChange(opt))
bgColor_menu.add_command(label="Gray", command=lambda opt="Gray": handleBgChange(opt))
bgColor_menu.add_command(label="White", command=lambda opt="White": handleBgChange(opt))



for index, option in enumerate(names, start=1):
    dropdown_menu.add_command(label=option, command=lambda opt=option: option_selected(opt))

fontStyle3 = tkFont.Font(family="Times New Roman", size=35)
fontStyle4 = tkFont.Font(family="Times New Roman", size=30)


date = datetime.datetime.now()
date = date.strftime("%x")
now = date

timeDisplay = Label(rightFrame, bg="lightgray", text=now, font=fontStyle3,fg=color)
timeDisplay.grid(row=22,column=0,sticky=E)
dateDisplay = Label(rightFrame, bg="lightgray", text=date, font=fontStyle4,fg=color)
dateDisplay.grid(row=21,column=0,sticky=E)


def play():
    global now, timeDisplay, color
    x = datetime.datetime.now()
    now = (x.strftime("%X"))
    timeDisplay.grid_forget()
    timeDisplay = Label(rightFrame, bg="lightgray", text=now, font=fontStyle3,fg=color)
    timeDisplay.grid(row=18,pady=20,column=0,stick=E)
    rightFrame.after(200, play)
play()

# Add dropdown menu to Settings menu
cities_menu.add_cascade(label="Cities", menu=dropdown_menu)
settings_menu.add_cascade(label="Background Colors", menu=bgColor_menu)


# Add Settings menu to the menu bar
menu_bar.add_cascade(label="City", menu=cities_menu)
menu_bar.add_cascade(label="Settings", menu=settings_menu)

# Attach menu to window
window.config(menu=menu_bar)

# Start the GUI event loop
window.mainloop()
