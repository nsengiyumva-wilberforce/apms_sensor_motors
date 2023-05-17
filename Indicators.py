import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_PIN_BLUE = 2  # Use GPIO 18 for the LED
LED_PIN_GREEN = 3  # Use GPIO 18 for the LED
GPIO.setup(LED_PIN_BLUE, GPIO.OUT)
GPIO.setup(LED_PIN_GREEN, GPIO.OUT)

# Turn the LED on and off
while True:
    GPIO.output(LED_PIN_BLUE, GPIO.HIGH)  # Turn the LED on
    GPIO.output(LED_PIN_GREEN, GPIO.LOW)  # Turn the LED off
    time.sleep(0.5)  # Wait for 1 second
    GPIO.output(LED_PIN_BLUE, GPIO.LOW)  # Turn the LED off
    GPIO.output(LED_PIN_GREEN, GPIO.HIGH)  # Turn the LED on
    time.sleep(0.5)  # Wait for 1 second
