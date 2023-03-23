from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

# this method generates a query for a specific place to extract weather data using web scraping in python
# it returns multiple values of scraping it, such as, temp, precipitation, humidity, and wind speed
def get_weather(place):
    url = f"https://www.google.com/search?q=weather+in+{place}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    temp = soup.find("span", class_="wob_t").text
    precipitation = soup.find("span", id="wob_pp").text[:2]
    humidity = soup.find("span", id="wob_hm").text[:2]
    wind_speed = soup.find("span", id="wob_ws").text[:2]
    return temp, precipitation, humidity, wind_speed


# this method loads a particular set of rides and their video links from a json object for the particular place dependant on the temperature
# it loads rides to be done in cold weather if live temperature is less 10 Celsius
# else it loads rides to be done in a hot temperature
def setArray(temperature, place):
        f = open("activities.json")
        data = json.load(f)
        if int(temperature) < 10:
            return data[place]["low"] 
        else:
             return data[place]["high"]
        

# this function takes a temperature as an argument and return the image of a cloud if the temp is less than 10 deg celsius
# else it returns an image of a sun
def setImage(temperature):
    if temperature < 10:
        return "cold.png"
    else:
        return  "hot.png"
        


#the entry point to the web application
@app.route("/")
def index():
    temperature, precipitation, humidity, wind_speed = get_weather("London")
         
         # all the values that are to be used are passed on as arguments to the webpage
    return render_template("index.html", temperature=temperature, precipitation = precipitation.replace("%", ""), humidity = humidity, wind_speed = wind_speed, image = setImage(int(temperature)))


#the webpage which showcases the list of recommended rides 
@app.route("/weather", methods=["POST"])
def weather():
    place = request.form["place"]
    temperature, precipitation, humidity, wind_speed = get_weather(place)
    
    # setting the values of all the variables to be used on the webpage of weather.html
    return render_template("weather.html", place=place, temperature=temperature, precipitation = precipitation.replace("%",""), humidity = humidity, wind_speed = wind_speed, image = setImage(int(temperature)), array=setArray(temperature, place))


if __name__ == "__main__":
    app.run(debug=True)
