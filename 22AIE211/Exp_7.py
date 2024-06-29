import time

# Import necessary libraries
import RPi.GPIO as GPIO

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define pin numbers for sensors and actuators
sensor_pin = 17
actuator_pin = 18

# Set pin modes
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(actuator_pin, GPIO.OUT)

# Function to lock the door
def lock_door():
    GPIO.output(actuator_pin, GPIO.HIGH)
    print("Door locked")

# Function to unlock the door
def unlock_door():
    GPIO.output(actuator_pin, GPIO.LOW)
    print("Door unlocked")

# Function to collect and analyze sensor data
def collect_and_analyze_data():
    while True:
        if GPIO.input(sensor_pin) == GPIO.HIGH:
            lock_door()
            sensor_data = GPIO.input(sensor_pin)
            print("Sensor data:", sensor_data)
        else:
            unlock_door()
            sensor_data = GPIO.input(sensor_pin)
            print("Sensor data:", sensor_data)
        time.sleep(0.1)

# Main program loop
try:
    collect_and_analyze_data()

# Clean up GPIO on program exit
except KeyboardInterrupt:
    GPIO.cleanup()