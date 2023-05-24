# import required libraries
import RPi.GPIO as GPIO
import time
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
#LCD COMMANDS FROM THE KEYPAD
password = "APMS123"
lcd = LCD()

# these GPIO pins are connected to the keypad
# change these according to your connections!
L1 = 7
L2 = 8
L3 = 25
L4 = 27

C1 = 23
C2 = 22
C3 = 15
C4 = 14

# Initialize the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

# Make sure to configure the input pins to use the internal pull-down resistors
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column
def safe_exit(signum, frame):
    exit(1)
def print_to_lcd(value):
    try:
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
        lcd.text(value, 1)
        pause()
    except KeyboardInterrupt:
        pass
    finally:
        lcd.clear()
def get_password():
    password = ""
    while True:
        input_key = None
        while input_key is None:
            input_key = readLine(L2, ["4", "5", "6", "B"])
        if input_key == "#":
            break
        password += input_key
        print_to_lcd("*" * len(password))
        time.sleep(0.2)
    return password

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(characters[0])
    if(GPIO.input(C2) == 1):
        print(characters[1])
    if(GPIO.input(C3) == 1):
        print(characters[2])
        print_to_lcd(characters[2])
    if(GPIO.input(C4) == 1):
        print(characters[3])
        
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        # call the readLine function for each row of the keypad
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.1)
        lcd.text("Enter Password", 1)
        get_password()
except KeyboardInterrupt:
    print("\nApplication stopped!")    
