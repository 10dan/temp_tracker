import RPi.GPIO as GPIO
import time
import sensing
import threading

GPIO.setmode(GPIO.BCM)

button_pin = 23
GPIO.setup(button_pin, GPIO.IN)

lock = threading.Lock()

def button_callback(channel):
    if lock.acquire(False):
        try:
            if GPIO.input(button_pin) == GPIO.HIGH:  # Check if button is currently being pressed
                print(f"Button pressed, GPIO pin {channel} signal on.")
                result = sensing.take_measurment()
                print(result)
        finally:
            lock.release() 

GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback, bouncetime=200)

try:
    while True:
        time.sleep(0.1)
        pass
except KeyboardInterrupt:
    print("ancelled.") # ^Cancelled 
    GPIO.cleanup()
