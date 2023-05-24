import requests

url = 'https://apms-production.up.railway.app/api/water'
myobj = {'waterLevelReading': 17.9, 'systemId': 'U003'}

x = requests.post(url, json = myobj)

print(x.text)


