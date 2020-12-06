import obd
from obd_gui import (
    window,
    conn_lbl,
    mph_lbl,
    rpm_lbl,
    rpm_bar,
    shift_lbl,
    coolant_temp_lbl,
    engine_load_lbl,
    air_temp_lbl,
    throttle_pos_lbl,
    timing_adv_lbl,
)


# Methods for updating stats
def new_speed(raw_speed):
    kph = str(raw_speed).split(" ")[0]
    mph = str(int(float(kph) * 0.6214))
    mph_lbl.configure(text=mph + " MPH")


def new_rpm(raw_rpm):
    rpm = str(raw_rpm).split(".")[0]
    rpm_int = int(rpm)
    rpm_lbl.configure(text=rpm + " RPM")
    bar_num = int((rpm_int / 6800) * 100)
    rpm_bar["value"] = bar_num
    if rpm_int >= 4600:
        rpm_bar["style"] = "red.Horizontal.TProgressbar"
        shift_lbl.configure(text="SHIFT", bg="red")
    if rpm_int < 4600:
        rpm_bar["style"] = "green.Horizontal.TProgressbar"
        shift_lbl.configure(text="", bg=rpm_lbl.cget("background"))


def new_coolant_temp(raw_coolant_temp):
    coolant_temp = "Coolant Temp.\n" + str(raw_coolant_temp).split("deg")[0] + "C"
    coolant_temp_lbl.configure(text=coolant_temp)


def new_engine_load(raw_engine_load):
    load = str(raw_engine_load).split(".")[0]
    load_int = int(load)
    engine_load = load + "% Load"
    engine_load_lbl.configure(text=engine_load)
    if load_int >= 85:
        engine_load_lbl.configure(bg="red")
    if load_int < 85:
        engine_load_lbl.configure(bg=rpm_lbl.cget("background"))


def new_intake_temp(raw_intake_temp):
    intake_temp = "Intake Air Temp.\n" + str(raw_intake_temp).split(" deg")[0] + " C"
    air_temp_lbl.configure(text=intake_temp)


def new_throttle_pos(raw_throttle_pos):
    throttle_pos = "Throttle Position:\n" + str(raw_throttle_pos).split(".")[0] + "%"
    throttle_pos_lbl.configure(text=throttle_pos)


def new_timing_adv(raw_timing_adv):
    timing_adv = "Timing Advance:\n" + str(raw_timing_adv).split("deg")[0] + " deg."
    timing_adv_lbl.configure(text=timing_adv)


# def new_obd_voltage(raw_obd_voltage):
# 	obd_voltage_status = str(raw_obd_voltage)
# 	voltage_lbl.configure(text=obd_voltage_status)
# def new_fuel_status(raw_fuel_status):
# 	fuel_status = str(raw_fuel_status)
# 	fuel_status_lbl.configure(text=fuel_status)


try:
    # Start async connection to OBD adapter
    #connection = obd.Async()
    #connection = obd.Async(baudrate=9600)
    #connection = obd.Async(baudrate=19200)
    #connection = obd.Async(baudrate=38400)
    #connection = obd.Async(baudrate=115200)
    #connection = obd.Async(baudrate=9600,delay_cmds=0)
    #connection = obd.Async(baudrate=19200,delay_cmds=0)
    #connection = obd.Async(baudrate=38400,delay_cmds=0)
    connection = obd.Async(baudrate=115200,delay_cmds=0)

    # Set up codes to watch with callbacks
    connection.watch(obd.commands.SPEED, callback=new_speed)
    connection.watch(obd.commands.RPM, callback=new_rpm)
    connection.watch(obd.commands.COOLANT_TEMP, callback=new_coolant_temp)
    connection.watch(obd.commands.ENGINE_LOAD, callback=new_engine_load)
    connection.watch(obd.commands.INTAKE_TEMP, callback=new_intake_temp)
    connection.watch(obd.commands.THROTTLE_POS, callback=new_throttle_pos)
    connection.watch(obd.commands.TIMING_ADVANCE, callback=new_timing_adv)
    # connection.watch(obd.commands.ELM_VOLTAGE, callback=new_obd_voltage)
    # connection.watch(obd.commands.FUEL_STATUS, callback=new_fuel_status)

    # Start monitoring
    connection.start()
    conn_lbl.configure(text=connection.status())
except Exception:
    conn_lbl.configure(text="ERROR CONNECTING")

# Start display
window.mainloop()
