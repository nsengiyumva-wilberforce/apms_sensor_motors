import Adafruit_DHT
import requests
import time
import RPi.GPIO as GPIO

#endpoint for temperature transmission
url = 'https://apms-production.up.railway.app/api/temperature/current/1'

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
    # Use read_retry method. This will retry up to 15 times to
    # get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if(temperature < 29):
        GPIO.output(LED_PIN_BLUE, GPIO.HIGH)  # Turn the LED off
        GPIO.output(LED_PIN_RED, GPIO.LOW)  # Turn the LED on
        time.sleep(0.5)  # Wait for 1 second
        GPIO.output(LED_PIN_BLUE, GPIO.LOW)  # Turn the LED on
        time.sleep(0.5)  # Wait for 1 second
        
    if(temperature >= 29):
        GPIO.output(LED_PIN_RED, GPIO.HIGH)  # Turn the LED on
        GPIO.output(LED_PIN_BLUE, GPIO.LOW)  # Turn the LED off
        time.sleep(0.5)  # Wait for 1 second
        GPIO.output(LED_PIN_RED, GPIO.LOW)  # Turn the LED on
        time.sleep(0.5)  # Wait for 1 second
        
    if humidity is not None and temperature is not None:
        myobj = {'temperatureReading': temperature, 'systemId': 'T001'}
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        x = requests.put(url, json = myobj)
        print(x.text)        
    else:
        print('Failed to get reading. Try again!')

