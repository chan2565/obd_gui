import obd, time
from obd_gui import *

# Methods for updating stats
# Column 0
def new_speed(raw_speed):
	kph = str(raw_speed).split(' ')[0]
	mph = str(int(float(kph) * 0.6214))
	mph_lbl.configure(text=mph + " MPH")
def new_rpm(raw_rpm):
	rpm = str(raw_rpm).split('.')[0]
	rpm_int = int(rpm)
	rpm_lbl.configure(text=rpm + " RPM")
	bar_num = int((rpm_int / 3000) * 100)
	rpm_bar['value'] = bar_num
	if rpm_int >= 3000:
		rpm_bar['style'] = 'red.Horizontal.TProgressbar'
		shift_lbl.configure(text="SHIFT", bg="red")
	if rpm_int < 3000:
		rpm_bar['style'] = 'green.Horizontal.TProgressbar'
		shift_lbl.configure(text="", bg="")
def new_obd_voltage(raw_obd_voltage):
	obd_voltage_status = str(raw_obd_voltage)
	voltage_lbl.configure(text=obd_voltage_status)
def new_fuel_status(raw_fuel_status):
	fuel_status = str(raw_fuel_status)
	fuel_status_lbl.configure(text=fuel_status)
# Column 1
def new_coolant_temp(raw_coolant_temp):
	coolant_temp = "Coolant Temp.\n" + str(raw_coolant_temp)
	coolant_temp_lbl.configure(text=coolant_temp)
def new_engine_load(raw_engine_load):
	load = str(raw_engine_load).split('.')[0]
	load_int = int(load)
	engine_load = str(raw_engine_load) + " Load"
	engine_load_lbl.configure(text=engine_load)
	engine_load_bar['value'] = load_int
	if load_int >= 85:
		rpm_bar['style'] = 'red.Horizontal.TProgressbar'
	if load_int < 85:
		rpm_bar['style'] = 'green.Horizontal.TProgressbar'
def new_intake_temp(raw_intake_temp):
	intake_temp = str(raw_intake_temp)
	air_temp_lbl.configure(text=intake_temp)
def new_throttle_pos(raw_throttle_pos):
	throttle_pos = str(raw_throttle_pos)
	throttle_pos_lbl.configure(text=throttle_pos)
def new_timing_adv(raw_timing_adv):
	timing_adv = str(raw_timing_adv)
	timing_adv_lbl.configure(text=timing_adv)

try:
	# Start async connection to OBD adapter
	#connection = obd.Async(baudrate=9600)
	connection = obd.Async()

	# Set up codes to watch with callbacks
	# Column 0
	connection.watch(obd.commands.SPEED, callback=new_speed)
	connection.watch(obd.commands.RPM, callback=new_rpm)
	connection.watch(obd.commands.ELM_VOLTAGE, callback=new_obd_voltage)
	connection.watch(obd.commands.FUEL_STATUS, callback=new_fuel_status)
	# Column 1
	connection.watch(obd.commands.COOLANT_TEMP, callback=new_coolant_temp)
	connection.watch(obd.commands.ENGINE_LOAD, callback=new_engine_load)
	connection.watch(obd.commands.INTAKE_TEMP, callback=new_intake_temp)
	connection.watch(obd.commands.THROTTLE_POS, callback=new_throttle_pos)
	connection.watch(obd.commands.TIMING_ADVANCE, callback=new_timing_adv)

	# Start monitoring
	connection.start()
	conn_lbl.configure(text=connection.status())
except:
	conn_lbl.configure(text="ERROR CONNECTING")

# Start display
window.mainloop()
