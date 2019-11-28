from tkinter import Tk, ttk, Label, Button

# Create window
window = Tk()
window.title("OBD DISPLAY")
window.geometry('720x480')
window.attributes("-fullscreen", True)

## Styles
# Create green progress bar style
rpm_style_green = ttk.Style()
rpm_style_green.theme_use('default')
rpm_style_green.configure("green.Horizontal.TProgressbar", background='green')
# Create red progress bar style
rpm_style_red = ttk.Style()
rpm_style_red.theme_use('default')
rpm_style_red.configure("red.Horizontal.TProgressbar", background='red')


## Column 0
# Connection label
conn_lbl = Label(window, text="Connecting...", font=('Courier New', 14), padx=5, pady=5)
conn_lbl.grid(column=0, row=0, sticky="nsew")

# MPH label
mph_lbl = Label(window, text="00 MPH", font=('Courier New', 64), padx=5, pady=5)
mph_lbl.grid(column=0, row=1, sticky="nsew")

# RPM label
rpm_lbl = Label(window, text="0000 RPM", font=('Courier New', 48), padx=5, pady=5)
rpm_lbl.grid(column=0, row=2, sticky="nsew")

# RPM bar
rpm_bar = ttk.Progressbar(window, length=250, style='green.Horizontal.TProgressbar')
rpm_bar['value'] = 10
rpm_bar.grid(column=0, row=3, sticky="nsew")

# Shift label
shift_lbl = Label(window, text="--", font=('Courier New', 14), fg='black')
shift_lbl.grid(column=0, row=4, sticky="nsew")

# OBD voltage label
#voltage_lbl = Label(window, text="00.00 V", font=('Courier New', 14), fg='black')
#voltage_lbl.grid(column=0, row=5, sticky="nsew")

# Fuel status label
#fuel_status_lbl = Label(window, text="Fuel Status: --", font=('Courier New', 8))
#fuel_status_lbl.grid(column=0, row=6, sticky="nsew")

## Column 1
# Quit button
quit_btn = Button(window, text="Quit", font=('Courier New', 14), fg='black', bg='red', command=window.destroy)
quit_btn.grid(column=1, row=0, sticky="e")

# Coolant temperature label
coolant_temp_lbl = Label(window, text="Coolant Temp.\n--- C", font=('Courier New', 32), padx=5, pady=5)
coolant_temp_lbl.grid(column=1, row=1, sticky="nsew")

# Engine load label
engine_load_lbl = Label(window, text="000% Load", font=('Courier New', 48), padx=5, pady=5)
engine_load_lbl.grid(column=1, row=2, sticky="nsew")

# Engine load bar
engine_load_bar = ttk.Progressbar(window, length=250, style='green.Horizontal.TProgressbar')
engine_load_bar['value'] = 10
engine_load_bar.grid(column=1, row=3, sticky="nsew")

# Intake air temperature label
air_temp_lbl = Label(window, text="Intake Air Temp.\n--- C", font=('Courier New', 14), padx=5, pady=5)
air_temp_lbl.grid(column=1, row=4, sticky="nsew")

# Throttle position label
throttle_pos_lbl = Label(window, text="Throttle Position:\n--", font=('Courier New', 14))
throttle_pos_lbl.grid(column=1, row=5, sticky="nsew")

# Timing advance label
timing_adv_lbl = Label(window, text="Timing Advance:\n--", font=('Courier New', 14))
timing_adv_lbl.grid(column=1, row=6, sticky="nsew")

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
