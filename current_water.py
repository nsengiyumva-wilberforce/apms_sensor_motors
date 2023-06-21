import serial
import RPi.GPIO as GPIO
import requests
import time

url = 'https://apms-production.up.railway.app/api/water/current/1'

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_PIN_GREEN = 21  # Use GPIO 18 for the LED
LED_PIN_ORANGE = 20  # Use GPIO 18 for the LED
GPIO.setup(LED_PIN_GREEN, GPIO.OUT)
GPIO.setup(LED_PIN_ORANGE, GPIO.OUT)
gpio=14
# Configure GPIO
GPIO.setup(gpio, GPIO.OUT)
# Set up serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust the port and baud rate if necessary
# Read a line from the serial port
line = int(ser.readline().decode().strip())

# Convert the line to an integer (assuming the Arduino sends integer values)

def get_water_level():
    return line

def get_water_sensor_status(sensorState):
    if(sensorState ==1):
        print("Water sensor activated")
        GPIO.output(gpio, GPIO.HIGH)
    elif(sensorState ==2):
        print("Water sensor deactivated")
        GPIO.output(gpio, GPIO.LOW)

try:
    #myobj = {'waterLevelReading': line, 'systemId': 'W001'}
    #print("Received sensor value: {}".format(line))
    #x = requests.put(url, json = myobj)
    #print(x.text)
    if(line < 29):
        GPIO.output(LED_PIN_GREEN, GPIO.HIGH)  # Turn the LED off
        GPIO.output(LED_PIN_ORANGE, GPIO.LOW)  # Turn the LED on
        time.sleep(0.5)  # Wait for 1 second
        GPIO.output(LED_PIN_GREEN, GPIO.LOW)  # Turn the LED on
        time.sleep(0.5)  # Wait for 1 second
    if(line >= 29):
        GPIO.output(LED_PIN_ORANGE, GPIO.HIGH)  # Turn the LED on
        GPIO.output(LED_PIN_GREEN, GPIO.LOW)  # Turn the LED off
        time.sleep(0.5)  # Wait for 1 second
        GPIO.output(LED_PIN_ORANGE, GPIO.LOW)  # Turn the LED on
        time.sleep(0.5)  # Wait for 1 second


except ValueError:
    print("Invalid data received.")

    #permissions
    #sudo usermod -a -G dialout <username>
    #sudo chmod a+rw /dev/ttyUSB0
    #ls /dev/tty*

