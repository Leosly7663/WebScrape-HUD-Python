# pip install urllib
import urllib
import urllib.request
import urllib.error
from urllib.request import Request, urlopen
import urllib.request

import requests
from os.path  import basename


# pip install beautifulsoup4
from bs4 import BeautifulSoup, SoupStrainer

def onlineValidate():
    try:
        internetCheck = urllib.request.urlopen('https://www.youtube.com/')
    except urllib.error.URLError:
        print("Internet connection failed please check network connection settings")
        return False
    else:
        if str(internetCheck.getcode()) == "200":
            return True
        

def scrapeCity(cityNames, cityLinks):
    # sends a request to the website then returns the HTML infor to be sorted for usable info
    weatherReq = Request('https://weather.gc.ca/forecast/canada/index_e.html?id=ON', headers={'User-Agent': 'Mozilla/5.0'})
    weatherDoc = urlopen(weatherReq).read()


    soup = BeautifulSoup(weatherDoc, 'html.parser')
        # by giving it a class to look for you can get the specific information you need much easier
    for i in range(3):
        soupText = soup.find_all(class_="list-unstyled col-sm-4")[i]
        for element in soupText:
            if element != "\n":
                cityNames.append(element.get_text())
        for link in soupText.find_all('a', href=True):
            cityLinks.append("https://weather.gc.ca/" + link['href'])

        # we have scraped the foundational information for the selection menu presenting you with where you want to get the weather info from
                
        # In a production env this will be modularized, and its output routed to a file store where the main program will call on instead of having to rescrape every second

def scrapeWeather(links, mainForecast, futureForecast, forecastGifs):

     # sends a request to the website then returns the HTML infor to be sorted for usable info
    weatherReq = Request(links, headers={'User-Agent': 'Mozilla/5.0'})
    weatherDoc = urlopen(weatherReq).read()


    soup = BeautifulSoup(weatherDoc, 'html.parser')
        # by giving it a class to look for you can get the specific information you need much easier
    
    import re
    elements = soup.find_all(class_="hidden-xs row no-gutters")
    loop = 0

    # Iterate through elements and filter strings
    for element in elements:
        # Iterate through the strings of the element
        for string in element.stripped_strings:
            # Check if the string matches the regex pattern
            loop += 1
            if re.match("^", string): 
                # alright hear me out here
                # the files are always formatted the same way and who tf is updating weather.gc.ca 
                # so its not the worst idea to just pick out what I want instead of making a horribly complicated regex filter
                # if you've dug this deep into my code to review it, you obv know what you're doing and we both know theres a better way to do this
                # but im not getting paid for this and I'm a full time student so cherry picking our info is how we're doing it <3
                if loop in {5,6,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34}:
                    mainForecast.append(string)

    loop = 0

    
    #okay now i just want to steal their cute emojis
    images = soup.findAll('img')
    for image in images:
        # Print image source
        if re.search(r"\.gif$", image['src']):
            forecastGifs.append("https://weather.gc.ca/" + image['src'])

    for i in range(7):
        elements = soup.find_all(class_="div-column")[i]
        for element in elements:
            for string in element.stripped_strings:
                # Check if the string matches the regex pattern
                loop += 1
                if re.match("^", string): 
                    futureForecast[i].append(string)
        
         # write the gifs to a file and store in in temp
        with open("temp/"+ str(i) + "_" + basename(forecastGifs[i]), "wb") as f:
            f.write(requests.get(forecastGifs[i]).content)

    #['Sat', '3', 'Feb', '1', '°', 'C', 'Mainly sunny', 'Night', '-13', '°', 'C', 'A few clouds']  


    print(mainForecast)
    print(futureForecast)
    
   