import requests

url = 'https://apms-production.up.railway.app/api/feed'
myobj = {'feedLevelReading': 18.1, 'systemId': 'U003'}

x = requests.post(url, json = myobj)

print(x.text)

