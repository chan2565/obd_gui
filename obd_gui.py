from tkinter import Tk, ttk, Label, Button
import os

# Create Window
window = Tk()
window.title("OBD DISPLAY")
window.geometry("720x480")
window.attributes("-fullscreen", True)
window.configure(background="black")

# Styles
# Create green progress bar style
rpm_style_green = ttk.Style()
rpm_style_green.theme_use("default")
rpm_style_green.configure("green.Horizontal.TProgressbar", background="green", troughcolor="black")
# Create red progress bar style
rpm_style_red = ttk.Style()
rpm_style_red.theme_use("default")
rpm_style_red.configure("red.Horizontal.TProgressbar", background="red", troughcolor="black")

# Base Labels
base_conn_lbl = "Connecting..."
base_mph_lbl =  ""
base_coolant_temp_lbl = "Cool.: "
base_air_temp_lbl = "Intake: "
base_throttle_pos_lbl = "Thrtl: "
base_shift_lbl = "Not Yet"
active_shift_lbl = "SHIFT~!"
base_rpm_lbl = ""
base_engine_load_lbl = "Load: "
base_timing_adv_lbl = "Time: "


# Column 0
# Connection label
conn_lbl = Label(window, text=base_conn_lbl, font=("Courier New", 14), padx=5, pady=5, fg="white", bg="black")
conn_lbl.grid(column=0, row=0, sticky="nsew")

# RPM bar
rpm_bar = ttk.Progressbar(window, length=250, style="green.Horizontal.TProgressbar")
rpm_bar["value"] = 10
rpm_bar.grid(column=0, row=1, columnspan=2, sticky="nsew")

# MPH label
mph_lbl = Label(window, text=base_mph_lbl + "00 MPH", font=("Courier New", 64), padx=5, pady=5, fg="white", bg="black")
mph_lbl.grid(column=0, row=2, sticky="nsew")

# Coolant temperature label
coolant_temp_lbl = Label(
    window, text=base_coolant_temp_lbl + "--- C", font=("Courier New", 30), padx=5, pady=5, fg="white", bg="black"
)
coolant_temp_lbl.grid(column=0, row=3, sticky="nsew")

# Intake air temperature label
air_temp_lbl = Label(
    window, text=base_air_temp_lbl + "--- C", font=("Courier New", 30), padx=5, pady=5, fg="white", bg="black"
)
air_temp_lbl.grid(column=0, row=4, sticky="nsew")

# Quit button
quit_btn = Button(
    window,
    text="Quit",
    font=("Courier New", 30),
    fg="white",
    bg="black",
    command=window.destroy,
)
quit_btn.grid(column=0, row=6, sticky="nsew")


# Column 1
# Shift label
shift_lbl = Label(window, text=base_shift_lbl, font=("Courier New", 16), fg="white", bg="black")
shift_lbl.grid(column=1, row=0, sticky="nsew")

# Shift bar (cont.) column=1, row=1

# RPM label
rpm_lbl = Label(window, text=base_rpm_lbl + "0000 RPM", font=("Courier New", 48), padx=5, pady=5, fg="white", bg="black")
rpm_lbl.grid(column=1, row=2, sticky="nsew")

# Engine load label
engine_load_lbl = Label(
    window, text=base_engine_load_lbl + "000%", font=("Courier New", 30), padx=5, pady=5, fg="white", bg="black"
)
engine_load_lbl.grid(column=1, row=3, sticky="nsew")

# Timing advance label
timing_adv_lbl = Label(window, text=base_timing_adv_lbl + "-- deg.", font=("Courier New", 30), fg="white", bg="black")
timing_adv_lbl.grid(column=1, row=4, sticky="nsew")

# Throttle position label
throttle_pos_lbl = Label(
    window, text=base_throttle_pos_lbl + "--%", font=("Courier New", 30), fg="white", bg="black"
)
throttle_pos_lbl.grid(column=1, row=5, sticky="nsew")


# Shutdown function
def shut_dwn():
    os.system("sudo shutdown now -h")


# Shutdown Button
shutdown_btn = Button(
    window,
    text="Shut Down",
    font=("Courier New", 30),
    fg="white",
    bg="black",
    command=shut_dwn,
)
shutdown_btn.grid(column=1, row=6, sticky="nsew")

# Set weights
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)


# Methods for updating stats
def new_speed(raw_speed):
    kph = str(raw_speed).split(" ")[0]
    mph = str(int(float(kph) * 0.6214))
    mph_lbl.configure(text=base_mph_lbl + mph + " MPH")


def new_rpm(raw_rpm):
    rpm = str(raw_rpm).split(".")[0]
    rpm_int = int(rpm)
    rpm_lbl.configure(text=base_rpm_lbl + rpm + " RPM")
    bar_num = int((rpm_int / 6800) * 100)
    rpm_bar["value"] = bar_num
    if rpm_int >= 4600:
        rpm_bar["style"] = "red.Horizontal.TProgressbar"
        shift_lbl.configure(text=active_shift_lbl, bg="red", fg="black")
    if rpm_int < 4600:
        rpm_bar["style"] = "green.Horizontal.TProgressbar"
        shift_lbl.configure(text=base_shift_lbl, fg="white", bg="black")


def new_coolant_temp(raw_coolant_temp):
    coolant_temp = str(raw_coolant_temp).split("deg")[0]
    int_coolant_temp = int(coolant_temp)
    if int_coolant_temp < 85:
        coolant_temp_lbl.configure(fg="black", bg="yellow")
    elif (int_coolant_temp >= 85) and (int_coolant_temp < 100):
        coolant_temp_lbl.configure(fg="black", bg="green")
    elif (int_coolant_temp >= 100):
        coolant_temp_lbl.configure(fg="black", bg="red")
    coolant_temp_txt = base_coolant_temp_lbl + coolant_temp + " C"
    coolant_temp_lbl.configure(text=coolant_temp_txt)


def new_engine_load(raw_engine_load):
    load = str(raw_engine_load).split(".")[0]
    load_int = int(load)
    engine_load = base_engine_load_lbl + load + "%"
    engine_load_lbl.configure(text=engine_load)
    if load_int >= 85:
        engine_load_lbl.configure(fg="black", bg="red")
    if load_int < 85:
        engine_load_lbl.configure(fg="white", bg="black")


def new_intake_temp(raw_intake_temp):
    intake_temp = base_air_temp_lbl + str(raw_intake_temp).split(" deg")[0] + " C"
    air_temp_lbl.configure(text=intake_temp)


def new_throttle_pos(raw_throttle_pos):
    throttle_pos = base_throttle_pos_lbl + str(raw_throttle_pos).split(".")[0] + "%"
    throttle_pos_lbl.configure(text=throttle_pos)


def new_timing_adv(raw_timing_adv):
    timing_adv = base_timing_adv_lbl + str(raw_timing_adv).split("deg")[0] + " deg."
    timing_adv_lbl.configure(text=timing_adv)


# def new_obd_voltage(raw_obd_voltage):
# 	obd_voltage_status = str(raw_obd_voltage)
# 	voltage_lbl.configure(text=obd_voltage_status)


# def new_fuel_status(raw_fuel_status):
# 	fuel_status = str(raw_fuel_status)
# 	fuel_status_lbl.configure(text=fuel_status)
