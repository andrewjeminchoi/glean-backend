import hashlib
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def mock_user():
    u1 = {
        "username" : "achoo"
    }
    return u1

def get_user(request):
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

    # Get username from request
    try:
        user = request["username"].encode('utf-8')

        m = hashlib.md5()
        m.update(user)
        user_id = str(int(m.hexdigest(), 16))[0:12]
        print(user_id)

        # doc_ref = db.collection(u'user-store').document(user_id)
        # doc_ref.set({
        #     "username" : str(user), 
        #     "id" : str(user_id)
        # })

        print({
            "username" :  request["username"], 
            "id" : str(user_id)
        })



        return {
            "username" : str(user), 
            "id" : str(user_id)
        }

    except Exception as e:
        print(e)
        return {}

get_user(mock_user())

'''

curl -d '{"username":"achoo3"}' -H 'Content-Type: application/json' 'https://us-central1-cuhacks21.cloudfunctions.net/main-test'

'''