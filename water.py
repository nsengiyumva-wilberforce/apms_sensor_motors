import serial
import RPi.GPIO as GPIO
import requests

url = 'https://apms-production.up.railway.app/api/water/'

GPIO.setmode(GPIO.BCM)
# Set up serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust the port and baud rate if necessary

# Read a line from the serial port
line = ser.readline().decode().strip()

# Convert the line to an integer (assuming the Arduino sends integer values)
try:
    myobj = {'waterLevelReading': line, 'systemId': 'W001'}
    print("Received sensor value: {}".format(line))
    x = requests.post(url, json = myobj)
    print(x.text)

except ValueError:
    print("Invalid data received.")

    #permissions
    #sudo usermod -a -G dialout <username>
    #sudo chmod a+rw /dev/ttyUSB0
    #ls /dev/tty*
