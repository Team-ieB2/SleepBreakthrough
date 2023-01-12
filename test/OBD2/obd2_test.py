import obd
from obd import OBDStatus
import time, csv
import os

f = open("data.csv", "w")
writer = csv.writer(f, lineterminator="\n")

connection = obd.OBD("/dev/rfcomm0")
print (connection.status())

if connection.status() == OBDStatus.CAR_CONNECTED:
	writer.writerow(["rpm", "speed"])
	while(True):
		try:
			rpm = connection.query(obd.commands.RPM)
			speed = connection.query(obd.commands.SPEED)
			writer.writerow([rpm.value.magnitude, speed.value.magnitude])
			print (rpm.value.magnitude, speed.value.magnitude)
			# time.sleep(.2)
		except KeyboardInterrupt:
			pass
else:
	connection.close()
