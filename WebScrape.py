# pip install urllib
import urllib
import urllib.request
import urllib.error
from urllib.request import Request, urlopen
import urllib.request


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

    # empty loops and dictionaries to track and store info
    cityNames = []
    cityLinks = []
    loop = 1
    loop2 = 1
    loop3 = 1
    info = {}
    timeDict = {}
    temp = {}
    weatherStuff = {}
    weather = {}
    conditions = {}

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

        print(cityNames)
        print(cityLinks)


cityNames = []
cityLinks = []
scrapeCity(cityNames, cityLinks)