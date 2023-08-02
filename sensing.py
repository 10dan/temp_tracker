import time
from monitor import TemperatureMonitor
from db_connect import DatabaseConnection

monitor = TemperatureMonitor()
db_connection = DatabaseConnection()

try:
    start = time.time()
    while True:
        temp = monitor.read_temp()
        print(monitor)
        monitor.add_temp(temp)
        time.sleep(1)
        print(time.time() - start)
        if monitor.check_stable():
            print(f"time till stable: {time.time() - start}")
            break
except KeyboardInterrupt:
    print("Interrupted by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    db_connection.close()
