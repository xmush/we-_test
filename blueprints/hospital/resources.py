import json
from flask import Blueprint
from flask_restful import Api, Resource, marshal
from .model import Hospital
from blueprints import app, hospital, db
from flask_orator import  jsonify
from helper.mylocation import Location
import math

bp_hospital = Blueprint('Hospital', __name__)
api = Api(bp_hospital)

class HospitalList(Resource) :
    def __init__(self) :
        pass

    def get(self) :
        # hopitals = Hospital.take(100).get()
        hopitals = db.table('hospital_list').select(db.raw('longitude, latitude, status')).take(100).get();

        app.logger.debug('DEBUG : %s', hopitals)

        return jsonify(hopitals)
        # return marshal(hospital, Hospital.response_fields), 200

class NearbyHospitals(Resource) :
    def __init__(self) :
        pass

    def get(self) :

        my_location = Location.getMyLocation()

        lat = str(my_location['latitude'])
        lon = str(my_location['longitude'])

        covered_id = []

        result = [];

        distance = 1

        max_result_element = 25

        max_search_distance = 100
        
        while len(result) <= max_result_element and distance < max_search_distance :

            ids = "("+ ','.join(str(e) for e in covered_id) +")"

            # hopitals = []

            if(len(covered_id) == 0) :
                hopitals = db.select("select * FROM ( SELECT *,  ( ( ( acos( sin(( "+ lat +" * pi() / 180)) * sin(( `latitude` * pi() / 180)) + cos(( "+ lat +" * pi() /180 )) * cos(( `latitude` * pi() / 180)) * cos((( 106.794586 - `longitude`) * pi()/180))) ) * 180/pi() ) * 60 * 1.1515 * 1.609344 ) as distance FROM `hospital_list` ) hospital_list WHERE distance <= "+ str(distance) +" order by distance;");
            else :
                hopitals = db.select("select * FROM ( SELECT *,  ( ( ( acos( sin(( "+ lat +" * pi() / 180)) * sin(( `latitude` * pi() / 180)) + cos(( "+ lat +" * pi() /180 )) * cos(( `latitude` * pi() / 180)) * cos((( 106.794586 - `longitude`) * pi()/180))) ) * 180/pi() ) * 60 * 1.1515 * 1.609344 ) as distance FROM `hospital_list` ) hospital_list WHERE id not in "+ ids +" and distance <= "+ str(distance) +" order by distance;");
            

            covered_id.extend([item['id'] for item in hopitals])

            result.extend(hopitals)

            distance += 1

        result = result[0:max_result_element]

        for item in result :
            item['distance'] = str(round(item['distance'], 2))+ ' Km'

        result_ = {
            "location" : {

                "longitude" : lon,
                "latitude" : lat
            },
            "result" : result,
            "search_distance" : str(distance) + " Km"
        }

        app.logger.debug('DEBUG : %s', result_)

        return jsonify(result_)

class MyLocation(Resource) :
    def __init__(self) :
        pass

    def get(self) :
        res = Location.getMyLocation()

        return res

api.add_resource(HospitalList, '/list', '')
api.add_resource(NearbyHospitals, '/nearby', '')
api.add_resource(MyLocation, '/my-location', '')