from flask import Flask
from flask import jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_voyager_data():
    scrape_url = "https://theskylive.com/voyager1-tracker"
    page_response = requests.get(scrape_url, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")
    distance_earth = soup.find('span', {'id': 'disearth'})
    distance_sun = soup.find('span', {'id': 'dissun'})
    speed_sun = soup.find('span', {'id': 'speedsun'})
    speed_earth = "17.0"
    speed_sun = "24.7"
    right_ascension = soup.find('span', {'id': 'ar'})
    declination = soup.find('span', {'id': 'dec'})

    data = {"distance_earth" : distance_earth.text, "distance_sun" : distance_sun.text, "speed_sun" : speed_sun, "speed_earth" : speed_earth,"right_ascension" : right_ascension.text, "declination" : declination.text}
    return data        

@app.route("/")
def voyager():
    return jsonify(get_voyager_data())

if __name__ == '__main__':
    app.run(debug=True)
