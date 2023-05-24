from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pe=26
rec=19
GPIO.setup(pe,GPIO.OUT)
GPIO.setup(rec,GPIO.OUT)
GPIO.output(pe,0)
GPIO.output(rec,0)
def aufnahme():
    sleep(3)
    print("Aufnahme startet")
    GPIO.output(pe, 1)
    sleep(10)
    GPIO.output(pe, 0)
    sleep(5)
    print("Aufnahme beendet")
def abspielen():
    print("Wiedergabe startet")
    GPIO.output(rec, 1)
    sleep(1)
    GPIO.output(rec, 0)
    sleep(10)
    print("Wiedergabe beendet")
while True:
    aufnahme()
    abspielen()
