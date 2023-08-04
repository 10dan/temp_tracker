import RPi.GPIO as GPIO
import threading
import time
from monitor import TemperatureMonitor
from db_connect import DatabaseConnection
import webserver
from playsound import playsound

lock = threading.Lock()

button_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)

def play_end_noise():
    for _ in range(5):
        playsound('end.mp3')
        time.sleep(0.2)

def button_callback(channel):

    if lock.acquire(False):
        try:
            if (
                GPIO.input(button_pin) == GPIO.HIGH
            ):  # Check if button is currently being pressed
                playsound('start.mp3')
                take_measurment()
                play_end_noise()
                
        finally:
            lock.release()


GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback, bouncetime=200)

def take_measurment():
    monitor = TemperatureMonitor()
    while True:
        temp = monitor.read_temp()
        monitor.add_temp(temp)
        if monitor.check_stable():
            db_connection = DatabaseConnection()
            db_connection.log_temp(temp)
            db_connection.close()
            break
        time.sleep(1)


try:
    webserver.start_webserver()
except KeyboardInterrupt:
    GPIO.cleanup([button_pin])
