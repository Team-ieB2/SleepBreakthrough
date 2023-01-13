import obd
from obd import OBDStatus
import csv

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
            self.writer.writerow([name, value])

    def get_rpm(self):
        if self.connection.status() == OBDStatus.CAR_CONNECTED:
            rpm = self.connection.query(obd.commands.RPM)
            self.write_csv("RPM",rpm)
            return rpm
        else:
            pass

    def get_speed(self):
        if self.connection.status() == OBDStatus.CAR_CONNECTED:
            speed = self.connection.query(obd.commands.SPEED)
            self.write_csv("SPEED",speed)
            return speed
        else:
            pass

if __name__ == "__main__":
    obd2 = OBD2()
    # obd2.open_csv()
    while True:
        print(f"RPM: {obd2.get_rpm()}")
        print(f"SPEED: {obd2.get_speed()}")