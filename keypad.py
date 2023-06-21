# import required libraries
import RPi.GPIO as GPIO
import time
import current_water
import current_weight
import touch
import current_temperature
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
#LCD COMMANDS FROM THE KEYPAD
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

choice = ""

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
def print_to_lcd(value, line):
    try:
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
        lcd.text(value, line)
        pause()
    except KeyboardInterrupt:
        pass
    finally:
        lcd.clear()
password = ""
def readPassword(line, characters, password):
    GPIO.output(line, GPIO.HIGH)
    if GPIO.input(C1) == 1:
        print(characters[0])
        password += characters[0]
    if GPIO.input(C2) == 1:
        print(characters[1])
        password += characters[1]
    if GPIO.input(C3) == 1:
        print(characters[2])
        password += characters[2]
    if GPIO.input(C4) == 1:
        print(characters[3])
        password += characters[3]
    GPIO.output(line, GPIO.LOW)
    return password

def readChoice(line, characters, choice):
    GPIO.output(line, GPIO.HIGH)
    if GPIO.input(C1) == 1:
        print(characters[0])
        choice = characters[0]
        lcd.text(characters[0], 4)
    if GPIO.input(C2) == 1:
        choice = characters[1]
        print(characters[1])
        lcd.text(characters[1], 4)
    if GPIO.input(C3) == 1:
        choice = characters[2]
        print(characters[2])
        lcd.text(characters[2], 4)
    if GPIO.input(C4) == 1:
        choice = characters[3]
        print(characters[3])
        lcd.text(characters[3], 4)
    GPIO.output(line, GPIO.LOW)
    return choice
def get_password():
    lcd.text("Enter Password", 1)
    password = ""
    while True:
        password = readPassword(L1, ["1", "2", "3", "A"], password)
        password = readPassword(L2, ["4", "5", "6", "B"], password)
        password = readPassword(L3, ["7", "8", "9", "C"], password)
        password = readPassword(L4, ["*", "0", "#", "D"], password)
        lcd.text(password, 2)  # Print password to LCD
        time.sleep(0.1)

        if len(password) == 5:
            if password == "*131#":
                lcd.clear()  # Clear the LCD screen
                lcd.text("Access granted", 1)
                lcd.clear()
                break;
            else:
                lcd.clear()  # Clear the LCD screen
                lcd.text("Wrong password", 1)
                time.sleep(2)
                lcd.clear()
                lcd.text("Enter Password", 1)
                password = ""
    return password

#function for deactivating and activating the sensor device
def activate_deactivate_sensor():
    switch_value=""
    while True:
        switch_value = readChoice(L1, ["1", "2", "3", "A"], switch_value) 
        switch_value = readChoice(L2, ["4", "5", "6", "B"], switch_value)
        switch_value = readChoice(L3, ["7", "8", "9", "C"], switch_value)
        switch_value = readChoice(L4, ["*", "0", "#", "D"], switch_value)
        if switch_value == "1":
            lcd.clear()
            lcd.text("Status", 1)
            lcd.text("switched on", 2)
            lcd.text("0. Back",3)
            touch.get_sensor_status(1)
            switch_sensor_display_option()
            break;
        elif switch_value == "2":
            lcd.clear()
            lcd.text("Status", 1)
            lcd.text("switched off", 2)
            lcd.text("0. Back",3)
            touch.get_sensor_status(2)
            #this is where we are going to trigger
            switch_sensor_display_option()
            break;
        elif switch_value =="0":
            lcd.clear()
            switch_sensor_display_option()
            break;
        
#fucntion for deactivating and activating the sensor device ends here
        
        
# function to display the switch options for various sensors
def switch_sensor_display_option():
    switch_option=""
    while True:
        switch_option = readChoice(L1, ["1", "2", "3", "A"], switch_option) 
        switch_option = readChoice(L2, ["4", "5", "6", "B"], switch_option)
        switch_option = readChoice(L3, ["7", "8", "9", "C"], switch_option)
        switch_option = readChoice(L4, ["*", "0", "#", "D"], switch_option)
        if switch_option == "1":
            lcd.clear()
            lcd.text("Temp sensor", 1)
            lcd.text("1. ON", 2)
            lcd.text("2. OFF ", 3)
            lcd.text("0. Back",4)
            activate_deactivate_sensor()
            break;
        elif switch_option == "2":
            lcd.clear()
            lcd.text("feed sensor", 1)
            lcd.text("1. ON", 2)
            lcd.text("2. OFF ", 3)
            lcd.text("0. Back",4)
            activate_deactivate_sensor()
            break;
        elif switch_option == "3":
            lcd.clear()
            lcd.text("water sensor", 1)
            lcd.text("1. ON", 2)
            lcd.text("2. OFF ", 3)
            lcd.text("0. Back",4)
            activate_deactivate_sensor()
            break;
        elif switch_option == "4":
            lcd.clear()
            lcd.text("--security--", 1)
            lcd.text("1. ON", 2)
            lcd.text("2. OFF ", 3)
            lcd.text("0. Back",4)
            activate_deactivate_sensor()
            break;
        elif switch_option =="0":
            lcd.clear()
            menu()
            break;

#function for displaying the switching option for various sensors ends here

def get_first_choice():
    print("entering choice")
    choice = ""
    while True:
        choice = readChoice(L1, ["1", "2", "3", "A"], choice)
        choice = readChoice(L2, ["4", "5", "6", "B"], choice)
        choice = readChoice(L3, ["7", "8", "9", "C"], choice)
        choice = readChoice(L4, ["*", "0", "#", "D"], choice)    
        lcd.text(choice, 4)
        # Print password to LCD
        print("choice", len(choice))
        #time.sleep(0.1)
        if len(choice) == 1:
            if choice == "1":
                # Clear the LCD screen
                lcd.text("1. Temperature", 1)
                lcd.text("2. Feed ", 2)
                lcd.text("3. Water", 3)
                lcd.text("4. Security 0. Back", 4)
                switch_sensor_display_option()   
                break;
            elif choice == "2":
                lcd.text("Temperature:" + str(current_temperature.get_temperature()) + "C", 1)
                lcd.text("Feed:{0:0.1f}".format(current_weight.get_feed_value()) + "Kg", 2)
                lcd.text("Water: " +str(current_water.get_water_level()) + "ml", 3)
                lcd.text("0.Back", 4)
                switch_sensor_display_option()  
                break;
            else:
                lcd.clear()  # Clear the LCD screen
                menu()
                choice = ""
                lcd.clear()
                break;
    return choice

def menu():
    lcd.text("MENU", 1)
    lcd.text("1. Configurations", 2)
    lcd.text("2. System Readings", 3)
    get_first_choice()
    
def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(characters[0])
    if(GPIO.input(C2) == 1):
        print(characters[1])
    if(GPIO.input(C3) == 1):
        print(characters[2])
    if(GPIO.input(C4) == 1):
        print(characters[3])        
    GPIO.output(line, GPIO.LOW)

    
try:
    get_password()
    menu()
    while True:
        # call the readLine function for each row of the keypad
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.1)
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\nApplication stopped!")    