import obd
from obd_gui import (
    window,
    new_speed,
    new_rpm,
    new_coolant_temp,
    new_engine_load,
    new_intake_temp,
    new_throttle_pos,
    new_timing_adv,
    conn_lbl,
)


try:
    # Start async connection to OBD adapter
    # connection = obd.Async(baudrate=9600)
    connection = obd.Async()

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
