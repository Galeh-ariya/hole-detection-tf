import requests

def send(name, lat, long):
    url  = 'http://localhost:8080/api/hole'
    body = {
        'name': name,
        'latitude': lat,
        'longitude': long
        }
    response = requests.post(url, json = body)