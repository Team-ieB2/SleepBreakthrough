import obd
from obd import OBDStatus
import csv
import datetime
import pytz
import sys

class OBD2():
    def __init__(self):
        try:
            self.connection = obd.OBD("/dev/rfcomm0")
            self.writer = None
            print(self.connection.status())
        except:
            pass

    def exit(self):
        self.connection.close()

    def open_csv(self, file_name: str = "data.csv"):
        try:
            f = open(file_name, "w")
            self.writer = csv.writer(f, lineterminator="\n")
        except:
            pass

    def write_csv(self, name, value):
        try:
            if self.writer:
                now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
                self.writer.writerow([now, name, value])
        except:
            pass

    def get_rpm(self):
        try:
            if self.connection.status() == OBDStatus.CAR_CONNECTED:
                rpm = self.connection.query(obd.commands.RPM)
                self.write_csv("RPM",rpm.value.magnitude)
                return rpm.value.magnitude
            else:
                pass
        except:
            pass

    def get_speed(self):
        try:
            if self.connection.status() == OBDStatus.CAR_CONNECTED:
                speed = self.connection.query(obd.commands.SPEED)
                self.write_csv("SPEED",speed.value.magnitude)
                if speed.value.magnitude is None:
                    return 0
                else:
                    return speed.value.magnitude
            else:
                pass
        except:
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