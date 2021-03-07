from twilio.rest import Client

# Twilio apis
account_sid = ''
auth_token = ''

def mock_user_req():
    s1 = {
        "user" : "achoo",
        "date" : 13,
        "start_time" : 9,
        "end_time" : 17
    }

    return s1

def farms():
    f1 = {
        "latitude": 41.675438,
        "longitude": -91.513312,
        "title": 'Calico Farm',
        "query": 'calico+farm',
        "placeId": 'ChIJSyR-c_lp5IcRPw1xizXHlu0',
        "preferred_times" : [12, 11]
    }

    f2 = {
        "coordinate": {
            "latitude": 41.631087,
            "longitude":-91.571399
        },
        "title": 'Lucky Star Farms',
        "query": 'lucky+star+farms',
        "placeId": 'ChIJ---GfHdH5IcRbsdgM8j32so',
        "preferred_times" : [16, 17]
    }
    return [f1, f2]

def schedule(request):
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
    client = Client(account_sid, auth_token)

    result = {
        "title" : '',
        "time" : ''
    }

    # print(data)
    user_prefs = {}
    user_times = [i for i in range(data["start_time"], data["end_time"])]
    user_prefs[data["user"]] = user_times

    u_times = set(user_times)
    # print(user_times)
    
    farm_prefs = {}
    for f in farms():
        farm_prefs[f["title"]] = f["preferred_times"]
        f_times = set(f["preferred_times"])
        if u_times & f_times:
            print(u_times & f_times)
            print(f["title"])

            result["time"] = list(u_times & f_times)[0]
            result["title"] = f["title"]
            break

    
    # print(farm_prefs, user_prefs)
    client.api.account.messages.create(
    to="+12135361436",
    from_="+12137696156",
    body="From Glean: Your appointment at {} is at {} :~)".format(result["title"], result["time"]))
    return result

# p = schedule(mock_user_req())
# print(p)

'''

curl -d '{"user" : "achoo","date" : 13, "start_time" : 14,"end_time" : 17}' -H 'Content-Type: application/json' 'https://us-central1-cuhacks21.cloudfunctions.net/scheduler'

'''