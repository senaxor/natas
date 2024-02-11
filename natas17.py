#!/bin/usr/bin/python3

import requests
import string

chars='0123456789'+ string.ascii_uppercase + string.ascii_lowercase
url = 'http://natas17.natas.labs.overthewire.org/'
username='natas17'
password_17="XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"
password_18=""

while len(password_17) < 33 :
    for i in chars :
        
        print("Testing :" + i)
        try:
        x = requests.post(url, data ={'username':'natas18'}, auth = (username,password_17))
        except reqeusts.
            print("We Found " + i)
            password_18+=i
            break

print(password_17)

