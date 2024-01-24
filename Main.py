import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

from PIL import Image, ImageTk

# pip install datetime
import datetime

# the weather report you never thought you needed

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# if you want to change the text colour because you find it hard to see change it here
color = "black"

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# establish a date time for the clock animation
now = datetime.datetime.now()

# these are default values incase a fetch fails and to establish their variable names
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

forcastTime2 = "null"
conditionsForcast2 = "null"
temperatureAndFeelsLikeForcast2 = "null"
otherStuffForcastA2 = "null"
otherStuffForcastB2 = "null"
otherStuffForcastC2 = "null"
otherStuffForcastD2 = "null"
otherStuffForcastE2 = "null"
otherStuffForcastF2 = "null"

forcastTime3 = "null"
conditionsForcast3 = "null"
temperatureAndFeelsLikeForcast3 = "null"
otherStuffForcastA3 = "null"
otherStuffForcastB3 = "null"
otherStuffForcastC3 = "null"
otherStuffForcastD3 = "null"
otherStuffForcastE3 = "null"
otherStuffForcastF3 = "null"

forcastTime4 = "null"
conditionsForcast4 = "null"
temperatureAndFeelsLikeForcast4 = "null"
otherStuffForcastA4 = "null"
otherStuffForcastB4 = "null"
otherStuffForcastC4 = "null"
otherStuffForcastD4 = "null"
otherStuffForcastE4 = "null"
otherStuffForcastF4 = "null"

forcastTime5 = "null"
conditionsForcast5 = "null"
temperatureAndFeelsLikeForcast5 = "null"
otherStuffForcastA5 = "null"
otherStuffForcastB5 = "null"
otherStuffForcastC5 = "null"
otherStuffForcastD5 = "null"
otherStuffForcastE5 = "null"
otherStuffForcastF5 = "null"

forcastTime6 = "null"
conditionsForcast6 = "null"
temperatureAndFeelsLikeForcast6 = "null"
otherStuffForcastA6 = "null"
otherStuffForcastB6 = "null"
otherStuffForcastC6 = "null"
otherStuffForcastD6 = "null"
otherStuffForcastE6 = "null"
otherStuffForcastF6 = "null"

forcastTime7 = "null"
conditionsForcast7 = "null"
temperatureAndFeelsLikeForcast7 = "null"
otherStuffForcastA7 = "null"
otherStuffForcastB7 = "null"
otherStuffForcastC7 = "null"
otherStuffForcastD7 = "null"
otherStuffForcastE7 = "null"
otherStuffForcastF7 = "null"

forcastTime8 = "null"
conditionsForcast8 = "null"
temperatureAndFeelsLikeForcast8 = "null"
otherStuffForcastA8 = "null"
otherStuffForcastB8 = "null"
otherStuffForcastC8 = "null"
otherStuffForcastD8 = "null"
otherStuffForcastE8 = "null"
otherStuffForcastF8 = "null"

forcastTime9 = "null"
conditionsForcast9 = "null"
temperatureAndFeelsLikeForcast9 = "null"
otherStuffForcastA9 = "null"
otherStuffForcastB9 = "null"
otherStuffForcastC9 = "null"
otherStuffForcastD9 = "null"
otherStuffForcastE9 = "null"
otherStuffForcastF9 = "null"

forcastTime10 = "null"
conditionsForcast10 = "null"
temperatureAndFeelsLikeForcast10 = "null"
otherStuffForcastA10 = "null"
otherStuffForcastB10 = "null"
otherStuffForcastC10 = "null"
otherStuffForcastD10 = "null"
otherStuffForcastE10 = "null"
otherStuffForcastF10 = "null"



window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.minsize(width=screen_width, height=screen_height)
window.resizable(width=True, height=True)
window.title("Weather")

# turns image names and size coordinates into usable photoimages
def makeImage(image,x,y):
    image1 = Image.open("assets/" + image + ".png")
    test = ImageTk.PhotoImage(image1.resize((x, y)))
    return test

start = makeImage("start",200,200)

win1 = Frame(window,width=screen_width,height=screen_height,bg="lightgray")

win1.pack()



win2 = Frame(window,width=screen_width,height=screen_height,bg="lightgray")
leftFrame = Frame(win2,bg="lightgray")
rightFrame = Frame(win2,bg="lightgray")

rightFrameR1 = Frame(rightFrame, bg="lightgray")
rightFrameR2 = Frame(rightFrame, bg="lightgray")
rightFrameR3 = Frame(rightFrame, bg="lightgray")
rightFrameR4 = Frame(rightFrame, bg="lightgray")
rightFrameR5 = Frame(rightFrame, bg="lightgray")
rightFrameR6 = Frame(rightFrame, bg="lightgray")
rightFrameR7 = Frame(rightFrame, bg="lightgray")
rightFrameR8 = Frame(rightFrame, bg="lightgray")
rightFrameR9 = Frame(rightFrame, bg="lightgray")
rightFrameR10 = Frame(rightFrame, bg="lightgray")

middleTopFrame = Frame(win2,bg="lightgray")
middleBottomFrame = Frame(win2,bg="lightgray")


'''
left side spans 1st column and 1-4 rows
right side is 4th column and 1-4 rows

middle top is 2-3rd column and 1-2 rows
middle bottom is 2-3rd column and 3-4 rows

left side is 1 column and 10 rows
temp will take up 2 rows and 1 for each other element
'''


fontStyle3 = tkFont.Font(family="Times New Roman", size=35)
fontStyle4 = tkFont.Font(family="Times New Roman", size=30)

def makeWin2():
    global color
    fontStyle = tkFont.Font(family="Times New Roman", size=25)
    fontStyle2 = tkFont.Font(family="Times New Roman", size=15)
    fontStyleSmall = tkFont.Font(family="Times New Roman", size=10)
    fontStyleBig = tkFont.Font(family="Times New Roman", size=70)

    # left side
    leftLabel = Label(leftFrame,text="Current Conditions:",font=fontStyle, bg="lightgray",fg=color)
    temperatureCurrent = Label(leftFrame,text=currentTemp,font=fontStyleBig, bg="lightgray",fg=color)
    feelsLikeCurrent = Label(leftFrame,text=currentFeel,font=fontStyle, bg="lightgray",fg=color)
    humidityCurrent = Label(leftFrame,text=currentHumidity,font=fontStyle, bg="lightgray",fg=color)
    windSpeedCurrent = Label(leftFrame,text=currentWind,font=fontStyle, bg="lightgray",fg=color)
    dewpointCurrent = Label(leftFrame,text=currentDewpoint,font=fontStyle, bg="lightgray",fg=color)
    pressureCurrent = Label(leftFrame,text=currentPressure,font=fontStyle, bg="lightgray",fg=color)
    precipitationCurrent = Label(leftFrame,text=currentPrecipitation,font=fontStyle, bg="lightgray",fg=color)
    visibilityCurrent = Label(leftFrame,text=currentVisibility,font=fontStyle, bg="lightgray",fg=color)

    # right side forcast next hour (one column)
    forcastTimeLabel = Label(rightFrameR1, text=forcastTime, font=fontStyle2, bg="lightgray",fg=color)
    conditionsForcastLabel = Label(rightFrameR1, text=conditionsForcast, font=fontStyle2, bg="lightgray",fg=color)
    temperatureAndFeelsLikeForcastLabel = Label(rightFrameR1, text=temperatureAndFeelsLikeForcast, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastALabel = Label(rightFrameR1, text=otherStuffForcastA, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastBLabel = Label(rightFrameR1, text=otherStuffForcastB, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastCLabel = Label(rightFrameR1, text=otherStuffForcastC, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastDLabel = Label(rightFrameR1, text=otherStuffForcastD, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastELabel = Label(rightFrameR1, text=otherStuffForcastE, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastFLabel = Label(rightFrameR1, text=otherStuffForcastF, font=fontStyleSmall, bg="lightgray",fg=color)

    forcastTime2Label = Label(rightFrameR2, text=forcastTime2, font=fontStyle2, bg="lightgray",fg=color)
    conditionsForcast2Label = Label(rightFrameR2, text=conditionsForcast2, font=fontStyle2, bg="lightgray",fg=color)
    temperatureAndFeelsLikeForcast2Label = Label(rightFrameR2, text=temperatureAndFeelsLikeForcast2, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastA2Label = Label(rightFrameR2, text=otherStuffForcastA2, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastB2Label = Label(rightFrameR2, text=otherStuffForcastB2, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastC2Label = Label(rightFrameR2, text=otherStuffForcastC2, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastD2Label = Label(rightFrameR2, text=otherStuffForcastD2, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastE2Label = Label(rightFrameR2, text=otherStuffForcastE2, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastF2Label = Label(rightFrameR2, text=otherStuffForcastF2, font=fontStyleSmall, bg="lightgray",fg=color)

    forcastTime3Label = Label(rightFrameR3, text=forcastTime3, font=fontStyle2, bg="lightgray",fg=color)
    conditionsForcast3Label = Label(rightFrameR3, text=conditionsForcast3, font=fontStyle2, bg="lightgray",fg=color)
    temperatureAndFeelsLikeForcast3Label = Label(rightFrameR3, text=temperatureAndFeelsLikeForcast3, font=fontStyleSmall,bg="lightgray",fg=color)
    otherStuffForcastA3Label = Label(rightFrameR3, text=otherStuffForcastA3, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastB3Label = Label(rightFrameR3, text=otherStuffForcastB3, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastC3Label = Label(rightFrameR3, text=otherStuffForcastC3, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastD3Label = Label(rightFrameR3, text=otherStuffForcastD3, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastE3Label = Label(rightFrameR3, text=otherStuffForcastE3, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastF3Label = Label(rightFrameR3, text=otherStuffForcastF3, font=fontStyleSmall, bg="lightgray",fg=color)


    forcastTime4Label = Label(rightFrameR4, text=forcastTime4, font=fontStyle2, bg="lightgray",fg=color)
    conditionsForcast4Label = Label(rightFrameR4, text=conditionsForcast4, font=fontStyle2, bg="lightgray",fg=color)
    temperatureAndFeelsLikeForcast4Label = Label(rightFrameR4, text=temperatureAndFeelsLikeForcast4, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastA4Label = Label(rightFrameR4, text=otherStuffForcastA4, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastB4Label = Label(rightFrameR4, text=otherStuffForcastB4, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastC4Label = Label(rightFrameR4, text=otherStuffForcastC4, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastD4Label = Label(rightFrameR4, text=otherStuffForcastD4, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastE4Label = Label(rightFrameR4, text=otherStuffForcastE4, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastF4Label = Label(rightFrameR4, text=otherStuffForcastF4, font=fontStyleSmall, bg="lightgray",fg=color)

    forcastTime5Label = Label(rightFrameR5, text=forcastTime5, font=fontStyle2, bg="lightgray",fg=color)
    conditionsForcast5Label = Label(rightFrameR5, text=conditionsForcast5, font=fontStyle2, bg="lightgray",fg=color)
    temperatureAndFeelsLikeForcast5Label = Label(rightFrameR5, text=temperatureAndFeelsLikeForcast5, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastA5Label = Label(rightFrameR5, text=otherStuffForcastA5, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastB5Label = Label(rightFrameR5, text=otherStuffForcastB5, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastC5Label = Label(rightFrameR5, text=otherStuffForcastC5, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastD5Label = Label(rightFrameR5, text=otherStuffForcastD5, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastE5Label = Label(rightFrameR5, text=otherStuffForcastE5, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastF5Label = Label(rightFrameR5, text=otherStuffForcastF5, font=fontStyleSmall, bg="lightgray",fg=color)

    forcastTime6Label = Label(rightFrameR6, text=forcastTime6, font=fontStyle2, bg="lightgray",fg=color)
    conditionsForcast6Label = Label(rightFrameR6, text=conditionsForcast6, font=fontStyle2, bg="lightgray",fg=color)
    temperatureAndFeelsLikeForcast6Label = Label(rightFrameR6, text=temperatureAndFeelsLikeForcast6, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastA6Label = Label(rightFrameR6, text=otherStuffForcastA6, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastB6Label = Label(rightFrameR6, text=otherStuffForcastB6, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastC6Label = Label(rightFrameR6, text=otherStuffForcastC6, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastD6Label = Label(rightFrameR6, text=otherStuffForcastD6, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastE6Label = Label(rightFrameR6, text=otherStuffForcastE6, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastF6Label = Label(rightFrameR6, text=otherStuffForcastF6, font=fontStyleSmall, bg="lightgray",fg=color)

    forcastTime7Label = Label(rightFrameR7, text=forcastTime7, font=fontStyle2, bg="lightgray",fg=color)
    conditionsForcast7Label = Label(rightFrameR7, text=conditionsForcast7, font=fontStyle2, bg="lightgray",fg=color)
    temperatureAndFeelsLikeForcast7Label = Label(rightFrameR7, text=temperatureAndFeelsLikeForcast7, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastA7Label = Label(rightFrameR7, text=otherStuffForcastA7, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastB7Label = Label(rightFrameR7, text=otherStuffForcastB7, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastC7Label = Label(rightFrameR7, text=otherStuffForcastC7, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastD7Label = Label(rightFrameR7, text=otherStuffForcastD7, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastE7Label = Label(rightFrameR7, text=otherStuffForcastE7, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastF7Label = Label(rightFrameR7, text=otherStuffForcastF7, font=fontStyleSmall, bg="lightgray",fg=color)

    forcastTime8Label = Label(rightFrameR8, text=forcastTime8, font=fontStyle2, bg="lightgray",fg=color)
    conditionsForcast8Label = Label(rightFrameR8, text=conditionsForcast8, font=fontStyle2, bg="lightgray",fg=color)
    temperatureAndFeelsLikeForcast8Label = Label(rightFrameR8, text=temperatureAndFeelsLikeForcast8, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastA8Label = Label(rightFrameR8, text=otherStuffForcastA8, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastB8Label = Label(rightFrameR8, text=otherStuffForcastB8, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastC8Label = Label(rightFrameR8, text=otherStuffForcastC8, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastD8Label = Label(rightFrameR8, text=otherStuffForcastD8, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastE8Label = Label(rightFrameR8, text=otherStuffForcastE8, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastF8Label = Label(rightFrameR8, text=otherStuffForcastF8, font=fontStyleSmall, bg="lightgray",fg=color)

    forcastTime9Label = Label(rightFrameR9, text=forcastTime9, font=fontStyle2, bg="lightgray",fg=color)
    conditionsForcast9Label = Label(rightFrameR9, text=conditionsForcast9, font=fontStyle2, bg="lightgray",fg=color)
    temperatureAndFeelsLikeForcast9Label = Label(rightFrameR9, text=temperatureAndFeelsLikeForcast9, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastA9Label = Label(rightFrameR9, text=otherStuffForcastA9, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastB9Label = Label(rightFrameR9, text=otherStuffForcastB9, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastC9Label = Label(rightFrameR9, text=otherStuffForcastC9, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastD9Label = Label(rightFrameR9, text=otherStuffForcastD9, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastE9Label = Label(rightFrameR9, text=otherStuffForcastE9, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastF9Label = Label(rightFrameR9, text=otherStuffForcastF9, font=fontStyleSmall, bg="lightgray",fg=color)

    forcastTime10Label = Label(rightFrameR10, text=forcastTime10, font=fontStyle2, bg="lightgray",fg=color)
    conditionsForcast10Label = Label(rightFrameR10, text=conditionsForcast10, font=fontStyle2, bg="lightgray",fg=color)
    temperatureAndFeelsLikeForcast10Label = Label(rightFrameR10, text=temperatureAndFeelsLikeForcast10, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastA10Label = Label(rightFrameR10, text=otherStuffForcastA10, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastB10Label = Label(rightFrameR10, text=otherStuffForcastB10, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastC10Label = Label(rightFrameR10, text=otherStuffForcastC10, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastD10Label = Label(rightFrameR10, text=otherStuffForcastD10, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastE10Label = Label(rightFrameR10, text=otherStuffForcastE10, font=fontStyleSmall, bg="lightgray",fg=color)
    otherStuffForcastF10Label = Label(rightFrameR10, text=otherStuffForcastF10, font=fontStyleSmall, bg="lightgray",fg=color)

    forcastTimeLabel.grid(row=1,column=1,padx=(0, 1))
    conditionsForcastLabel.grid(row=1,column=2,padx=(0, 1))
    temperatureAndFeelsLikeForcastLabel.grid(row=2,columnspan=2,column=1,padx=(0, 3))
    otherStuffForcastALabel.grid(row=1,column=3)
    otherStuffForcastBLabel.grid(row=1,column=4)
    otherStuffForcastCLabel.grid(row=1,column=5)
    otherStuffForcastDLabel.grid(row=2,column=3)
    otherStuffForcastELabel.grid(row=2,column=4)
    otherStuffForcastFLabel.grid(row=2,column=5)

    forcastTime2Label.grid(row=1, column=1, padx=(0, 1))
    conditionsForcast2Label.grid(row=1, column=2, padx=(0, 1))
    temperatureAndFeelsLikeForcast2Label.grid(row=2, columnspan=2, column=1, padx=(0, 3))
    otherStuffForcastA2Label.grid(row=1, column=3)
    otherStuffForcastB2Label.grid(row=1, column=4)
    otherStuffForcastC2Label.grid(row=1, column=5)
    otherStuffForcastD2Label.grid(row=2, column=3)
    otherStuffForcastE2Label.grid(row=2, column=4)
    otherStuffForcastF2Label.grid(row=2, column=5)

    forcastTime3Label.grid(row=1, column=1, padx=(0, 1))
    conditionsForcast3Label.grid(row=1, column=2, padx=(0, 1))
    temperatureAndFeelsLikeForcast3Label.grid(row=2, columnspan=2, column=1, padx=(0, 3))
    otherStuffForcastA3Label.grid(row=1, column=3)
    otherStuffForcastB3Label.grid(row=1, column=4)
    otherStuffForcastC3Label.grid(row=1, column=5)
    otherStuffForcastD3Label.grid(row=2, column=3)
    otherStuffForcastE3Label.grid(row=2, column=4)
    otherStuffForcastF3Label.grid(row=2, column=5)

    forcastTime4Label.grid(row=1, column=1, padx=(0, 1))
    conditionsForcast4Label.grid(row=1, column=2, padx=(0, 1))
    temperatureAndFeelsLikeForcast4Label.grid(row=2, columnspan=2, column=1, padx=(0, 3))
    otherStuffForcastA4Label.grid(row=1, column=3)
    otherStuffForcastB4Label.grid(row=1, column=4)
    otherStuffForcastC4Label.grid(row=1, column=5)
    otherStuffForcastD4Label.grid(row=2, column=3)
    otherStuffForcastE4Label.grid(row=2, column=4)
    otherStuffForcastF4Label.grid(row=2, column=5)

    forcastTime5Label.grid(row=1, column=1, padx=(0, 1))
    conditionsForcast5Label.grid(row=1, column=2, padx=(0, 1))
    temperatureAndFeelsLikeForcast5Label.grid(row=2, columnspan=2, column=1, padx=(0, 3))
    otherStuffForcastA5Label.grid(row=1, column=3)
    otherStuffForcastB5Label.grid(row=1, column=4)
    otherStuffForcastC5Label.grid(row=1, column=5)
    otherStuffForcastD5Label.grid(row=2, column=3)
    otherStuffForcastE5Label.grid(row=2, column=4)
    otherStuffForcastF5Label.grid(row=2, column=5)

    forcastTime6Label.grid(row=1, column=1, padx=(0, 1))
    conditionsForcast6Label.grid(row=1, column=2, padx=(0, 1))
    temperatureAndFeelsLikeForcast6Label.grid(row=2, columnspan=2, column=1, padx=(0, 3))
    otherStuffForcastA6Label.grid(row=1, column=3)
    otherStuffForcastB6Label.grid(row=1, column=4)
    otherStuffForcastC6Label.grid(row=1, column=5)
    otherStuffForcastD6Label.grid(row=2, column=3)
    otherStuffForcastE6Label.grid(row=2, column=4)
    otherStuffForcastF6Label.grid(row=2, column=5)

    forcastTime7Label.grid(row=1, column=1, padx=(0, 1))
    conditionsForcast7Label.grid(row=1, column=2, padx=(0, 1))
    temperatureAndFeelsLikeForcast7Label.grid(row=2, columnspan=2, column=1, padx=(0, 3))
    otherStuffForcastA7Label.grid(row=1, column=3)
    otherStuffForcastB7Label.grid(row=1, column=4)
    otherStuffForcastC7Label.grid(row=1, column=5)
    otherStuffForcastD7Label.grid(row=2, column=3)
    otherStuffForcastE7Label.grid(row=2, column=4)
    otherStuffForcastF7Label.grid(row=2, column=5)

    forcastTime8Label.grid(row=1, column=1, padx=(0, 1))
    conditionsForcast8Label.grid(row=1, column=2, padx=(0, 1))
    temperatureAndFeelsLikeForcast8Label.grid(row=2, columnspan=2, column=1, padx=(0, 3))
    otherStuffForcastA8Label.grid(row=1, column=3)
    otherStuffForcastB8Label.grid(row=1, column=4)
    otherStuffForcastC8Label.grid(row=1, column=5)
    otherStuffForcastD8Label.grid(row=2, column=3)
    otherStuffForcastE8Label.grid(row=2, column=4)
    otherStuffForcastF8Label.grid(row=2, column=5)

    forcastTime9Label.grid(row=1, column=1, padx=(0, 1))
    conditionsForcast9Label.grid(row=1, column=2, padx=(0, 1))
    temperatureAndFeelsLikeForcast9Label.grid(row=2, columnspan=2, column=1, padx=(0, 3))
    otherStuffForcastA9Label.grid(row=1, column=3)
    otherStuffForcastB9Label.grid(row=1, column=4)
    otherStuffForcastC9Label.grid(row=1, column=5)
    otherStuffForcastD9Label.grid(row=2, column=3)
    otherStuffForcastE9Label.grid(row=2, column=4)
    otherStuffForcastF9Label.grid(row=2, column=5)

    forcastTime10Label.grid(row=1, column=1, padx=(0, 1))
    conditionsForcast10Label.grid(row=1, column=2, padx=(0, 1))
    temperatureAndFeelsLikeForcast10Label.grid(row=2, columnspan=2, column=1, padx=(0, 3))
    otherStuffForcastA10Label.grid(row=1, column=3)
    otherStuffForcastB10Label.grid(row=1, column=4)
    otherStuffForcastC10Label.grid(row=1, column=5)
    otherStuffForcastD10Label.grid(row=2, column=3)
    otherStuffForcastE10Label.grid(row=2, column=4)
    otherStuffForcastF10Label.grid(row=2, column=5)

    leftLabel.grid(row=1,sticky=W,pady=0)
    temperatureCurrent.grid(row=2,sticky=W,pady=10)
    feelsLikeCurrent.grid(row=3,sticky=W,pady=10)
    humidityCurrent.grid(row=4,sticky=W,pady=10)
    windSpeedCurrent.grid(row=5,sticky=W,pady=10)
    dewpointCurrent.grid(row=6,sticky=W,pady=10)
    pressureCurrent.grid(row=7,sticky=W,pady=10)
    precipitationCurrent.grid(row=8,sticky=W,pady=10)
    visibilityCurrent.grid(row=9,sticky=W,pady=10)




rightFrameR1.grid(row=1,pady=6,sticky=E)
rightFrameR2.grid(row=2,pady=6,sticky=E)
rightFrameR3.grid(row=3,pady=6,sticky=E)
rightFrameR4.grid(row=4,pady=6,sticky=E)
rightFrameR5.grid(row=5,pady=6,sticky=E)
rightFrameR6.grid(row=6,pady=6,sticky=E)
rightFrameR7.grid(row=7,pady=6,sticky=E)
rightFrameR8.grid(row=8,pady=6,sticky=E)
rightFrameR9.grid(row=9,pady=6,sticky=E)
rightFrameR10.grid(row=10,pady=6,sticky=E)




# Display current conditions

placeholder = Label(middleTopFrame)

window.attributes("-transparentcolor", "lightgray")
window.attributes("-topmost", True)
window.overrideredirect(True)

date = datetime.datetime.now()
date = date.strftime("%x")

timeDisplay = Label(rightFrame, bg="lightgray", text=now, font=fontStyle3,fg=color)
timeDisplay.grid(row=12,sticky=E)
dateDisplay = Label(rightFrame, bg="lightgray", text=date, font=fontStyle4,fg=color)
dateDisplay.grid(row=11,pady=(335,0),sticky=E)

print(currentWeather)

conditionsDisplay = Label(leftFrame, bg="lightgray", text=currentWeather, font=fontStyle3,fg=color)
conditionsDisplay.grid(row=15,pady=(390,0),sticky=SW)



middleBottomFrame.grid(column=2,row=1,rowspan=4)
middleTopFrame.grid(column=2,row=2,rowspan=4,padx=577)

leftFrame.grid(column=1,row=1,sticky=NW)
rightFrame.grid(column=4,row=1,rowspan=4,sticky=NE)

def play():
    global now, timeDisplay
    x = datetime.datetime.now()
    now = (x.strftime("%X"))
    timeDisplay.grid_forget()
    timeDisplay = Label(rightFrame, bg="lightgray", text=now, font=fontStyle3)
    timeDisplay.grid(row=12,stick=E)
    rightFrame.after(10, play)

    
play()

mainloop()
