import datetime
import json
import urllib.request

def url_builder(lat, lon):
    api = "e2d7adc23db789fadf9c14618a930f52",
    unit = 'metric',

    return 'https://api.openweathermap.org/data/2.5/weather' + \
    '?units=' + unit + \
    '&APPID=' + api + \
    '&lat=' + str(lat) + \
    '&lon=' + str(lon)

def fetch_data(full_url):
    url = urllib.request.urlopen(full_url)
    output = url.read().decode('utf-8')
    return json.loads(output)

def time_converter(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).\
      strftime('%d %b %I:%M %p')

lat = 51.5074
lon = -0.1278

json_data = fetch_data(url_builder(lat, lon))

temperature = str(json_data['main']['temp'])
timestamp = time_converter(json_data['dt'])
description = json_data['weather'][0]['description']

print(json_data) 
print("current weather")
print(timestamp + " :" + temperature " : " + description)
