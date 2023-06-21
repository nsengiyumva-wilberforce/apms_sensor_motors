import Adafruit_DHT
import requests
import time
import RPi.GPIO as GPIO

#endpoint for temperature transmission
url = 'https://apms-production.up.railway.app/api/temperature/'

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_PIN_BLUE = 19  # Use GPIO 18 for the LED
LED_PIN_RED = 26  # Use GPIO 18 for the LED
GPIO.setup(LED_PIN_BLUE, GPIO.OUT)
GPIO.setup(LED_PIN_RED, GPIO.OUT)

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio=17

# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.



while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
        myobj = {'temperatureReading': temperature, 'systemId': 'U001'}
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        x = requests.post(url, json = myobj)
        print(x.text)       
    else:
        print('Failed to get reading. Try again!')
