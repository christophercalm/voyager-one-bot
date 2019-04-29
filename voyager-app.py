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
    data = {"distance_earth" : distance_earth.text, "distance_sun" : distance_sun.text}
    return data        

@app.route("/")
def hello():
    return jsonify(get_voyager_data())

if __name__ == '__main__':
    app.run(debug=True)
