import json

with open('user.json', 'r') as file:
    data = json.load(file)

    users = data['users']

    for user in users:
        with open('passwords.txt', 'a') as f:
            password_str = user['password']
            f.write(f"{password_str}\n")
    
    print('Done!')