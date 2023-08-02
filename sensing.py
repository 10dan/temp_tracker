import time
from monitor import TemperatureMonitor
from db_connect import DatabaseConnection

monitor = TemperatureMonitor()
db_connection = DatabaseConnection()


try:
    while True:
        temp = monitor.read_temp()
        print(monitor)
        monitor.add_temp(temp)
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrupted by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    db_connection.close()