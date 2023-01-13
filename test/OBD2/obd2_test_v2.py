import obd
from obd import OBDStatus
import csv
import datetime
import pytz
import sys

class OBD2():
    def __init__(self):
        self.connection = obd.OBD("/dev/rfcomm0")
        self.writer = None
        print(self.connection.status())

    def exit(self):
        self.connection.close()

    def open_csv(self, file_name: str = "data.csv"):
        f = open(file_name, "w")
        self.writer = csv.writer(f, lineterminator="\n")

    def write_csv(self, name, value):
        if self.writer:
            now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
            self.writer.writerow([now, name, value])

    def get_rpm(self):
        if self.connection.status() == OBDStatus.CAR_CONNECTED:
            rpm = self.connection.query(obd.commands.RPM)
            self.write_csv("RPM",rpm.value.magnitude)
            return rpm.value.magnitude
        else:
            pass

    def get_speed(self):
        if self.connection.status() == OBDStatus.CAR_CONNECTED:
            speed = self.connection.query(obd.commands.SPEED)
            self.write_csv("SPEED",speed.value.magnitude)
            return speed.value.magnitude
        else:
            pass

if __name__ == "__main__":
    obd2 = OBD2()
    try:
        # obd2.open_csv()
        while True:
            print(f"RPM: {obd2.get_rpm()}")
            print(f"SPEED: {obd2.get_speed()}")
    except:
        obd2.exit()
        sys.exit()