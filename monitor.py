import os
import time
import glob


class TemperatureMonitor:
    def __init__(self):
        self.temps = []
        self.max_len = 10
        self.threshold = 0.06
        self.base_dir = "/sys/bus/w1/devices/"
        self.device_folder = glob.glob(self.base_dir + "28*")[0]
        self.device_file = self.device_folder + "/w1_slave"
        os.system("modprobe w1-gpio")
        os.system("modprobe w1-therm")

    def __str__(self):
        length = len(self.temps)
        avg = sum(self.temps) / length if self.temps else "N/A"
        stable = "True" if self.check_stable() else "False"
        avg_string = f"{avg:.2f}" if isinstance(avg, (int, float)) else "N/A"
        return f"Length: {length}, " f"Average: {avg_string}, " f"Stable: {stable}"

    def add_temp(self, temp):
        if len(self.temps) == self.max_len:
            self.temps.pop(0)
        self.temps.append(temp)

    def check_stable(self):
        if len(self.temps) < self.max_len:
            return False
        if max(self.temps) - min(self.temps) <= self.threshold:
            return sum(self.temps) / len(self.temps)
        return False

    def read_temp_raw(self):
        f = open(self.device_file, "r")
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != "YES":
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find("t=")
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2 :]
            temp_c = float(temp_string) / 1000.0
            return temp_c
