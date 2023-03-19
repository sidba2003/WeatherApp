from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)


def get_weather(place):
    url = f"https://www.google.com/search?q=weather+in+{place}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    temp = soup.find("span", class_="wob_t").text
    precipitation = soup.find("span", id="wob_pp").text[:1]
    humidity = soup.find("span", id="wob_hm").text[:2]
    wind_speed = soup.find("span", class_="wob_t").text[:2]
    return temp, precipitation, humidity, wind_speed

def setArray(temperature, place):
        f = open("activities.json")
        data = json.load(f)
        if int(temperature) <= 25:
            return data[place]["low"] 
        else:
             return data[place["high"]]
        


@app.route("/")
def index():
    temperature, precipitation, humidity, wind_speed = get_weather("London")
    return render_template("index.html", temperature=temperature, precipitation = precipitation, humidity = humidity, wind_speed = wind_speed)

@app.route("/weather", methods=["POST"])
def weather():
    place = request.form["place"]
    temperature, precipitation, humidity, wind_speed = get_weather(place)
    return render_template("weather.html", place=place, temperature=temperature, precipitation = precipitation, humidity = humidity, wind_speed = wind_speed, array=setArray(temperature, place))

if __name__ == "__main__":
    app.run(debug=True)
