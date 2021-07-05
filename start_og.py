import obd, asyncio, time
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


async def mainloop(connection):
    while True:
        speed_task = asyncio.create_task(new_speed(connection.query(obd.commands.SPEED)))
        rpm_task = asyncio.create_task(new_rpm(connection.query(obd.commands.RPM)))
        coolant_task = asyncio.create_task(new_coolant_temp(connection.query(obd.commands.COOLANT_TEMP)))
        load_task = asyncio.create_task(new_engine_load(connection.query(obd.commands.ENGINE_LOAD)))
        intake_task = asyncio.create_task(new_intake_temp(connection.query(obd.commands.INTAKE_TEMP)))
        throttle_task = asyncio.create_task(new_throttle_pos(connection.query(obd.commands.THROTTLE_POS)))
        timing_task = asyncio.create_task(new_timing_adv(connection.query(obd.commands.TIMING_ADVANCE)))
        await speed_task
        await rpm_task
        await coolant_task
        await load_task
        await intake_task
        await throttle_task
        await timing_task
        window.update_idletasks()
        window.update()
        time.sleep(0.1)

def start_connection():
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
        connection.watch(obd.commands.SPEED)
        connection.watch(obd.commands.RPM)
        connection.watch(obd.commands.COOLANT_TEMP)
        connection.watch(obd.commands.ENGINE_LOAD)
        connection.watch(obd.commands.INTAKE_TEMP)
        connection.watch(obd.commands.THROTTLE_POS)
        connection.watch(obd.commands.TIMING_ADVANCE)

        # Start monitoring
        connection.start()
        conn_lbl.configure(text=connection.status())
        return connection
    except Exception:
        conn_lbl.configure(text="ERROR CONNECTING")
        window.update()
        raise Exception("ERROR CONNECTING")

connection = start_connection()
asyncio.run(mainloop(connection))
