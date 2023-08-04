import RPi.GPIO as GPIO
import threading
import time
from monitor import TemperatureMonitor
from db_connect import DatabaseConnection
import webserver

lock = threading.Lock()
button_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)


def button_callback(channel):
    if lock.acquire(False):
        try:
            if (
                GPIO.input(button_pin) == GPIO.HIGH
            ):  # Check if button is currently being pressed
                print(f"Button pressed, GPIO pin {channel} signal on.")
                result = take_measurment()
                print(result)
        finally:
            lock.release()


GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback, bouncetime=200)


def take_measurment():
    monitor = TemperatureMonitor()
    db_connection = DatabaseConnection()
    start = time.time()
    while True:
        temp = monitor.read_temp()
        monitor.add_temp(temp)
        print(temp)
        if monitor.check_stable():
            db_connection.log_temp(temp)
            db_connection.close()
            return f"Measurement recorded in {time.time() - start:.2f}"

        time.sleep(1)

webserver.start_webserver()