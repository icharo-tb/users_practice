import requests
import json

def user_api():
    res = requests.get('https://dummyjson.com/users/')
    print(res.ok)

    res_json = res.json()

    with open('user.json', 'w') as f:
        data = json.dumps(res_json)
        file = f.write(data)
    
    return file

print(user_api())