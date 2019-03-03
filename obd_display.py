import obd, time
from obd_gui import *

# Methods for updating stats
def new_rpm(raw_rpm):
	rpm = raw_rpm.split('.')[0]
	rpm_lbl.configure(text=rpm + " RPM")
	bar_num = int((int(rpm) / 3000) * 100)
	rpm_bar['value'] = bar_num

def new_speed(raw_speed):
	kph = raw_speed.split(' ')[0]
	mph = str(int(float(kph) * 0.6214))
	mph_lbl.configure(text=mph + " MPH")

# Connect to OBD sensor
try:
	connection = obd.Async(baudrate=9600)
	connection.watch(obd.commands.RPM, callback=new_rpm)
	connection.watch(obd.commands.SPEED, callback=new_speed)
	connection.start()
	
	conn_lbl.configure(text=connection.status())
except:
	conn_lbl.configure(text="ERROR CONNECTING")

# Start display
window.mainloop()