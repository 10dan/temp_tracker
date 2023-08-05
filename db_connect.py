import psycopg2
import os
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
        self.cur.execute(
            sql.SQL("INSERT INTO room_temps (temperature) VALUES (%s)"), [temp]
        )
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
