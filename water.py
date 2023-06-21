import serial
import RPi.GPIO as GPIO
import requests
import time

# Define the GPIO pin connected to the TTP223 OUT pin
url = 'https://apms-production.up.railway.app/api/water/'

GPIO.setmode(GPIO.BCM)
# Set up serial connection

# Read a line from the serial port


while True:
    ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust the port and baud rate if necessary
    line = ser.readline().decode().strip()
    # Convert the line to an integer (assuming the Arduino sends integer values)
    try:
        #v = PI * r * r * h
        #v = 3.14 * 3.1 * 3.1 * 3
        # 90.5262cm^3
        #239units = 90.5262 mil
        #1unit = 0.379ml

        myobj = {'waterLevelReading': int(line)*0.379, 'systemId': 'W001'}
        print("Received sensor value: {}".format(int(line)*0.379))
        #x = requests.post(url, json = myobj)
        #print(x.text)

    except ValueError:
        print("Invalid data received.")

        #permissions
        #sudo usermod -a -G dialout <username>
        #sudo chmod a+rw /dev/ttyUSB0
        #ls /dev/tty*
