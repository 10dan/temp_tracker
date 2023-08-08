import psycopg2
import os
import datetime
from psycopg2 import sql


class DatabaseConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="temperature_tracking",
            user="dbadmin",
            password=os.getenv("DB_PASSWORD"),
            host="localhost",
        )
        self.cur = self.conn.cursor()

    def log_temp(self, temp):
        self.cur.execute(
            sql.SQL("INSERT INTO temperatures (temperature) VALUES (%s)"), [temp]
        )
        self.conn.commit()

    def get_all_body_temps(self):
        self.cur.execute("SELECT * FROM temperatures;")
        return self.cur.fetchall()
    
    def get_all_room_temps(self):
        self.cur.execute("SELECT * FROM room_temps;")
        return self.cur.fetchall()

    def log_room_temp(self, temp):
        # Fetch the most recent timestamp from the temperatures table
        self.cur.execute("SELECT time_stamp FROM temperatures WHERE id = (SELECT max(id) FROM temperatures);")
        result = self.cur.fetchone()

        if not result:
            self._insert_room_temp(temp)
            return

        latest_temp_time = result[0]
        current_time = datetime.datetime.now(datetime.timezone.utc)
        if (current_time - latest_temp_time).total_seconds() >= 1800: # 1800 = 30 mins
            self._insert_room_temp(temp)
        else:
            print("Reader needs more time to cool back to ambient temperature.")

    def _insert_room_temp(self, temp):
        self.cur.execute(
            sql.SQL("INSERT INTO room_temps (temperature) VALUES (%s)"), [temp]
        )
        self.conn.commit()


    def close(self):
        self.cur.close()
        self.conn.close()
