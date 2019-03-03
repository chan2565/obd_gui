import obd, time
from obd_gui import *

# Methods for updating stats
def new_rpm(raw_rpm):
	rpm = str(raw_rpm).split('.')[0]
	rpm_int = int(rpm)
	rpm_lbl.configure(text=rpm + " RPM")
	bar_num = int((rpm_int / 2500) * 100)
	rpm_bar['value'] = bar_num
	if rpm_int >= 2500:
		rpm_bar['style'] = 'red.Horizontal.TProgressbar'
		shift_lbl.configure(text="SHIFT")
	if rpm_int < 2500:
		rpm_bar['style'] = 'green.Horizontal.TProgressbar'
		shift_lbl.configure(text="")
def new_speed(raw_speed):
	kph = str(raw_speed).split(' ')[0]
	mph = str(int(float(kph) * 0.6214))
	mph_lbl.configure(text=mph + " MPH")
def new_air_status(raw_air_status):
	air_status = str(raw_air_status)
	air_status_lbl.configure(text=air_status)
def new_fuel_rate(raw_fuel_rate):
	fuel_rate = "Fuel Rate\n" + str(raw_fuel_rate)
	fuel_rate_lbl.configure(text=fuel_rate)
def new_oil_temp(raw_oil_temp):
	oil_temp = "Oil Temp.\n" + str(raw_oil_temp)
	oil_temp_lbl.configure(text=oil_temp)
def new_fuel_lvl(raw_fuel_lvl):
	fuel_lvl = str(raw_fuel_lvl)
	fuel_lvl_lbl.configure(text=fuel_lvl)
def new_fuel_type(raw_fuel_type):
	fuel_type = str(raw_fuel_type)
	fuel_type_lbl.configure(text=fuel_type)
def new_fuel_status(raw_fuel_status):
	fuel_status = str(raw_fuel_status)
	fuel_status_lbl.configure(text=fuel_status)

try:
	# Start async connection to OBD adapter
	connection = obd.Async(baudrate=9600)
	
	# Set up codes to watch with callbacks
	connection.watch(obd.commands.RPM, callback=new_rpm)
	connection.watch(obd.commands.SPEED, callback=new_speed)
	#connection.watch(obd.commands.AIR_STATUS, callback=new_air_status)
	#connection.watch(obd.commands.FUEL_RATE, callback=new_fuel_rate)
	#connection.watch(obd.commands.OIL_TEMP, callback=new_oil_temp)
	#connection.watch(obd.commands.FUEL_LEVEL, callback=new_fuel_lvl)
	#connection.watch(obd.commands.FUEL_TYPE, callback=new_fuel_type)
	#connection.watch(obd.commands.FUEL_STATUS, callback=new_fuel_status)
	
	# Start monitoring
	connection.start()
	conn_lbl.configure(text=connection.status())
except:
	conn_lbl.configure(text="ERROR CONNECTING")

# Start display
window.mainloop()
