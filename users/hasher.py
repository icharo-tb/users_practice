from password_hash import hash_password

hashed_lst = []

with open('passwords.txt', 'r+') as file:
    fh = file.readlines()
    for password in fh:
        striped_pass = password.rstrip()
        hashed_lst.append(hash_password(striped_pass))

with open('hashed_passwords.txt','wb') as f:
    for i in hashed_lst:
        data = i.decode('utf-8') + "\n"
        f.write(data.encode('utf-8'))