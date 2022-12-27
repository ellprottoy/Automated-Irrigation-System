import RPi.GPIO as GPIO
import time
import os
import datetime

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(irrigationPin, GPIO.OUT)

# Set up the light sensor (TSL2561)
tsl = Adafruit_TSL2561.TSL2561()

# Set the light threshold
LIGHT_THRESHOLD = 10

def main():
  while True:
    # Get the light level
    lightLevel = tsl.lux()

    # If the light level is below the threshold, turn on the irrigation system
    if lightLevel < LIGHT_THRESHOLD:
      GPIO.output(irrigationPin, True)
    else:
      GPIO.output(irrigationPin, False)

    # Print the current time and light level to the console
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"), lightLevel)

    # Wait 1 minute before taking the next reading
    time.sleep(60)

# Run the main function
if __name__ == "__main__":
  main()
