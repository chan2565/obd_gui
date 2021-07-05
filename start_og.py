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
    new_speed_async,
    new_rpm_async,
    new_coolant_temp_async,
    new_engine_load_async,
    new_intake_temp_async,
    new_throttle_pos_async,
    new_timing_adv_async,
    conn_lbl,
)


try:
    # Start async connection to OBD adapter
    connection = obd.Async()
    #connection = obd.Async(baudrate=9600)
    #connection = obd.Async(baudrate=19200)
    #connection = obd.Async(baudrate=38400)
    #connection = obd.Async(baudrate=115200)
    #connection = obd.Async(baudrate=9600,delay_cmds=0)
    #connection = obd.Async(baudrate=19200,delay_cmds=0)
    #connection = obd.Async(baudrate=38400,delay_cmds=0)
    #connection = obd.Async(baudrate=115200,delay_cmds=0)

    # Set up codes to watch with callbacks
    connection.watch(obd.commands.SPEED, callback=new_speed_async)
    connection.watch(obd.commands.RPM, callback=new_rpm_async)
    connection.watch(obd.commands.COOLANT_TEMP, callback=new_coolant_temp_async)
    connection.watch(obd.commands.ENGINE_LOAD, callback=new_engine_load_async)
    connection.watch(obd.commands.INTAKE_TEMP, callback=new_intake_temp_async)
    connection.watch(obd.commands.THROTTLE_POS, callback=new_throttle_pos_async)
    connection.watch(obd.commands.TIMING_ADVANCE, callback=new_timing_adv_async)
    # connection.watch(obd.commands.ELM_VOLTAGE, callback=new_obd_voltage)
    # connection.watch(obd.commands.FUEL_STATUS, callback=new_fuel_status)

    # Start monitoring
    connection.start()
    conn_lbl.configure(text=connection.status())
except Exception:
    conn_lbl.configure(text="ERROR CONNECTING")

# Start display
window.mainloop()
