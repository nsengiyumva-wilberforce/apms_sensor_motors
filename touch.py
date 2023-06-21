import RPi.GPIO as GPIO
import time

# Define the GPIO pin connected to the TTP223 OUT pin
TOUCH_PIN = 4
gpio=10
# Configure GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_PIN, GPIO.IN)
GPIO.setup(gpio, GPIO.OUT)
GPIO.output(gpio, GPIO.LOW)

def get_sensor_status(sensorState):
    if(sensorState ==1):
        GPIO.output(gpio, GPIO.HIGH)
        if GPIO.input(TOUCH_PIN) == GPIO.HIGH:
            print("Touch detected!")
        else:
            print("No touch detected.")
        print("switched on")
    elif(sensorState ==2):
        GPIO.output(gpio, GPIO.LOW)

#try:
 #   while True:
        # Check if the touch sensor is touched
  #      if GPIO.input(TOUCH_PIN) == GPIO.HIGH:
   #         print("Touch detected!")
    #    else:
     #       print("No touch detected.")
#
 #       time.sleep(0.1)  # Small delay before checking again

#except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
 #   GPIO.cleanup()
