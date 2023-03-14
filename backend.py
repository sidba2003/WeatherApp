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
    return temp

def setArray(temperature, place):
        f = open("activities.json")
        data = json.load(f)
        if int(temperature) <= 25:
            return data[place]["low"] 
        else:
             return data[place["high"]]
        


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    place = request.form["place"]
    temperature = get_weather(place)
    return render_template("weather.html", place=place, temperature=temperature, array=setArray(temperature, place))

if __name__ == "__main__":
    app.run(debug=True)
