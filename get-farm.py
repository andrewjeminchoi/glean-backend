import json


class LocationRequest(object):
    def __init__(self, min_lat, max_lat, min_lon, max_lon):
        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_lon = min_lon
        self.max_lon = max_lon


def mock_loc_req():
    r1 = {
        "minLat": 41.7180397,
        "maxLat": 41.8180398,
        "minLon": -91.4630380,
        "maxLon": -91.4630389
    }

def mock_farm():
    f1 = {
        "coordinate" : {
            "latitude" : 41.7180398,
            "longitude" : -91.4630386
        },
        "title" : "Wilson Orchard Farm",
        "query" : "wilsons+orchard+farm",
        "placeId": 'ChIJy94QyN1o5IcRrw1e7gEl5Ns',
        "address1": '4823 Dingleberry Rd NE #1, Iowa City, IA',
        "address2": '52240, United States'
    }
    return f1

def mock_farms():
    r = [{
        "coordinate": {
            "latitude": 41.631087,
            "longitude":-91.571399
        },
        "title": 'Lucky Star Farms',
        "query": 'lucky+star+farms',
        "placeId": 'ChIJ---GfHdH5IcRbsdgM8j32so',
        "address1": '2625 Hwy 1 SW, Iowa City, IA',
        "address2": '52240, United States'
        },
        {
        "coordinate": {
            "latitude": 41.675438,
            "longitude": -91.513312
        },
        "title": 'Calico Farm',
        "query": 'calico+farm',
        "placeId": 'ChIJSyR-c_lp5IcRPw1xizXHlu0',
        "address1": '1380 N Dodge St Ct, Iowa City, IA',
        "address2": '52245, United States'
        },
        {
        "coordinate": {
            "latitude": 41.7180398,
            "longitude": -91.4630386
        },
        "title": 'Wilson Orchard & Farm',
        "query": 'wilsons+orchard+farm',
        "placeId": 'ChIJy94QyN1o5IcRrw1e7gEl5Ns',
        "address1": '4823 Dingleberry Rd NE #1, Iowa City, IA',
        "address2": '52240, United States'
        }]

    return r

def insert_farms(db): 
    # # Insertion
    doc_ref = db.collection(u'farm-store').document("calico")
    doc_ref.set({
    "latitude": 41.675438,
    "longitude": -91.513312,
    "title": 'Calico Farm',
    "query": 'calico+farm',
    "placeId": 'ChIJSyR-c_lp5IcRPw1xizXHlu0',
    "address1": '1380 N Dodge St Ct, Iowa City, IA',
    "address2": '52245, United States'
    })

    doc_ref = db.collection(u'farm-store').document("lucky")
    doc_ref.set({
    "latitude": 41.631087,
    "longitude":-91.571399,
    "title": 'Lucky Star Farms',
    "query": 'lucky+star+farms',
    "placeId": 'ChIJ---GfHdH5IcRbsdgM8j32so',
    "address1": '2625 Hwy 1 SW, Iowa City, IA',
    "address2": '52240, United States'
    })

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def get_farms(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    data = request.get_json()
    print("REQUEST :" , data)

    # Let's setup a NoSQL firestore db
    try:
        firebase_admin.get_app()
    except ValueError as e:
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
            'projectId': 'cuhacks21' # TODO: CHANGE ME!
        })
    db = firestore.client()

    # Query db for farms within range of distance
    try:
        

        # farm_ref = db.collection(u'farm-store')
        # query_ref = cities_ref.where(u'state', u'==', u'CA')

        return {"resp" : "success"}

    except Exception as e:
        print(e)
        return {"resp" : "fail"}



'''

curl https://us-central1-cuhacks21.cloudfunctions.net/farm-loc

'''