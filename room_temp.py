from monitor import TemperatureMonitor
from db_connect import DatabaseConnection

monitor = TemperatureMonitor()
temp = monitor.read_temp()

db_connection = DatabaseConnection()
db_connection.log_room_temp(temp)
db_connection.close()