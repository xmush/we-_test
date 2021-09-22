import requests
from flask import json
from blueprints import app

class Location :
    def __init__(self) :
        pass

    def getMyLocation() :
        key = app.config['IPSTACK_KEY']
        url = app.config['IPSTACK_URL']

        result = requests.get(url+'check', params={'access_key' : key})

        response = result.json()

        lon_lat = {
            'longitude' : response['longitude'],
            'latitude' : response['latitude']

        }

        return lon_lat
