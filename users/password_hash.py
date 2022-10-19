import random
import string
import bcrypt
import array

def password_generator():

    MAX_LEN = random.randint(5,15)
    ASCII = string.ascii_letters
    DIGITS = string.digits
    SPEC = string.punctuation

    COMBINATION = ASCII + DIGITS + SPEC

    rand_digit = random.choice(DIGITS)
    rand_ascii = random.choice(ASCII)
    rand_spec = random.choice(SPEC)

    tem_pass = rand_ascii + rand_digit + rand_spec

    for i in range(MAX_LEN):
        tem_pass = tem_pass + random.choice(COMBINATION)

        tem_pass_lst = array.array('u', tem_pass)
        random.shuffle(tem_pass_lst)
    
    password = ''
    for x in tem_pass_lst:
        password = password + x
    
    return password

def hash_password(password=None, password_gen=False):

    if password_gen == True:
        password = password_generator().encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    else:
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed

if __name__ == '__main__':
    password = input('Enter password or type True: ')
    
    if password in ['True','true']:
        print(hash_password(password_gen=True))
    else:
        print(hash_password(password))