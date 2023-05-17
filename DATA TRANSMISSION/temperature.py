import requests

url = 'https://apms-production.up.railway.app/api/temperature/'
myobj = {'temperatureReading': 20.1, 'systemId': 'U001'}

x = requests.post(url, json = myobj)

print(x.text)
