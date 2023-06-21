import schedule
import time
import keypad
import mobile_sensor_control
import subprocess

def run_python_file1():
    # Use subprocess to run the first Python file
    subprocess.call(['python', 'keypad.py'])

def run_python_file2():
    # Use subprocess to run the second Python file
    subprocess.call(['python', 'mobile_sensor_control.py'])

schedule.every(10).minutes.do(run_python_file1)
schedule.every(15).minutes.do(run_python_file2)

while True:
    schedule.run_pending()
    time.sleep(1)
