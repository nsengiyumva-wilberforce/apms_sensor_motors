import RPi.GPIO as GPIO
import time

# Define the GPIO pin connected to the TTP223 OUT pin
TOUCH_PIN = 4

# Configure GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_PIN, GPIO.IN)

try:
    while True:
        # Check if the touch sensor is touched
        if GPIO.input(TOUCH_PIN) == GPIO.HIGH:
            print("Touch detected!")
        else:
            print("No touch detected.")

        time.sleep(0.1)  # Small delay before checking again

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
