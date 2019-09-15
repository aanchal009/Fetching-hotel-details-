from urllib.request import Request, urlopen
import json

url='http://mapsearch.justdis.com/v14082601/json/justdialapicat/hotels/koramangala/IN/bangalore/NA/13043647/77620617/100km/3/0'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

data = urlopen(req).read()
print(data)
info=json.loads(data)
print(info)

