import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin number
led_pin = 26

# Set up the GPIO pin for output
GPIO.setup(led_pin, GPIO.OUT)

try:
    # Loop indefinitely
    while True:
        # Turn on the LED
        GPIO.output(led_pin, GPIO.HIGH)
        
        # Delay for 1 second
        time.sleep(1)
        
        # Turn off the LED
        GPIO.output(led_pin, GPIO.LOW)
        
        # Delay for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO settings on Ctrl+C exit
    GPIO.cleanup()
