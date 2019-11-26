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
rpm_bar = ttk.Progressbar(window, length=250, style='red.Horizontal.TProgressbar')
rpm_bar['value'] = 10
rpm_bar.grid(column=0, row=3, sticky="nsew")

# Shift label
shift_lbl = Label(window, text="--", font=('Courier New', 14), fg='white', bg='red')
shift_lbl.grid(column=0, row=4, sticky="nsew")

# Air status label
air_status_lbl = Label(window, text="Air Status: Everything Nominal", font=('Courier New', 14))
air_status_lbl.grid(column=0, row=6, sticky="nsew")

## Column 1
# Quit button
quit_btn = Button(window, text="Quit", font=('Courier New', 14), fg='black', bg='red', command=window.destroy)
quit_btn.grid(column=1, row=0, sticky="e")

# Fuel rate label
fuel_rate_lbl = Label(window, text="Fuel Rate\n.23 L/h", font=('Courier New', 32), padx=5, pady=5)
fuel_rate_lbl.grid(column=1, row=1, sticky="nsew")

# Oil temperature label
oil_temp_lbl = Label(window, text="Oil Temp.\n100 C", font=('Courier New', 24), padx=5, pady=5)
oil_temp_lbl.grid(column=1, row=2, sticky="nsew")

# Fuel level bar
fuel_lvl_bar = ttk.Progressbar(window, length=250, style='green.Horizontal.TProgressbar')
fuel_lvl_bar['value'] = 10
fuel_lvl_bar.grid(column=1, row=3, sticky="nsew")

# Fuel level label
fuel_lvl_lbl = Label(window, text="Fuel: ---%", font=('Courier New', 14))
fuel_lvl_lbl.grid(column=1, row=4, sticky="nsew")

# Fuel type label
fuel_type_lbl = Label(window, text="Fuel Type: Premium etc.", font=('Courier New', 14))
fuel_type_lbl.grid(column=1, row=5, sticky="nsew")

# Fuel status label
fuel_status_lbl = Label(window, text="Fuel Status: Everything Nominal", font=('Courier New', 14))
fuel_status_lbl.grid(column=1, row=6, sticky="nsew")

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
