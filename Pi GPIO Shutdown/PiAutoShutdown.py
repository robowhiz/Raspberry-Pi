import RPi.GPIO as GPIO
import time
import os

ShutdownButton = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(ShutdownButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def shutdown():
    print("Shutdown initiated")
    # Add any custom shutdown tasks here
    os.system("sudo shutdown -h now")

GPIO.add_event_detect(ShutdownButton, GPIO.FALLING, callback=shutdown, bouncetime=2000)

while True:
    time.sleep(1)