import time
from monitor import TemperatureMonitor
from db_connect import DatabaseConnection

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


