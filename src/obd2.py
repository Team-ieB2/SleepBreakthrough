"""
obd2.py
OBD2 Controller.

Copyright (C) 2023 Team ieB2. All Rights Reserved.
"""
# -*- coding: utf-8 -*-
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
            f = open("./csv/" + file_name, "w")
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

    def get_rpm(self) -> int:
        try:
            if self.connection.status() == OBDStatus.CAR_CONNECTED:
                rpm = self.connection.query(obd.commands.RPM)
                self.write_csv("RPM",rpm.value.magnitude)
                return rpm.value.magnitude
            else:
                pass
        except:
            pass

    def get_speed(self) -> int:
        try:
            if self.connection.status() == OBDStatus.CAR_CONNECTED:
                speed = self.connection.query(obd.commands.SPEED)
                self.write_csv("SPEED",speed.value.magnitude)
                return speed.value.magnitude
            else:
                pass
        except:
            pass

    def get_connection_status(self):
        try:
            return self.connection.status()
        except:
            return OBDStatus.NOT_CONNECTED

    def is_connected(self) -> bool:
        if self.get_connection_status() == OBDStatus.CAR_CONNECTED:
            return True
        else:
            return False