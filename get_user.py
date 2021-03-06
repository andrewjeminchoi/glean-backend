import hashlib

# Accepts a REST call with user info

def mock_user_request():
    user_json = {
        "username" : "achoo2"
    }
    return user_json

def get_user(data):
    # Get username from request
    user = data["username"].encode('utf-8')

    m = hashlib.md5()
    m.update(user)
    user_id = str(int(m.hexdigest(), 16))[0:12]
    print(user_id)

get_user(mock_user_request())


'''
curl -d '{"username":"achoo"}' -H 'Content-Type: application/json' 'https://us-central1-cuhacks21.cloudfunctions.net/main-test'
 

https://us-central1-cuhacks21.cloudfunctions.net/main-test 

'''