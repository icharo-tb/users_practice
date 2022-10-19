import requests
import json

def dummy_api():
    res = requests.get('https://dummyapi.io/data/v1/user?limit=50', headers={'app-id': '634ee495d0434a9c4e7fbdf2'})
    
    res_json = res.json()

    with open('dummy_api_user.json', 'w') as f:
        data = json.dumps(res_json)
        file = f.write(data)
    
    return file

print(dummy_api())

def dummy_json():
    res = requests.get('https://dummyjson.com/users/')

    res_json = res.json()

    with open('user.json', 'w') as f:
        data = json.dumps(res_json)
        file = f.write(data)
    
    return file

print(dummy_json())