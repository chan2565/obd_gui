# Import base
from tkinter import *

# Imports for progress bar
from tkinter.ttk import Progressbar
from tkinter import ttk

# Create window
window = Tk()
window.title("OBD DISPLAY")
#window.geometry('800x480')
#window.geometry('400x240')
window.geometry('700x380')

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
conn_lbl = Label(window, text="Connecting...", font=('', 14), padx=5, pady=5)
conn_lbl.grid(column=0, row=0)
# MPH label
mph_lbl = Label(window, text="00 MPH", font=('', 64), padx=5, pady=5)
mph_lbl.grid(column=0, row=1)
# RPM label
rpm_lbl = Label(window, text="0000 RPM", font=('', 48), padx=5, pady=5)
rpm_lbl.grid(column=0, row=2)
# RPM bar
rpm_bar = Progressbar(window, length=250, style='red.Horizontal.TProgressbar')
rpm_bar['value'] = 10
rpm_bar.grid(column=0, row=3)
# Shift label
shift_lbl = Label(window, text="--", font=('', 14), fg='white', bg='red')
shift_lbl.grid(column=0, row=4)
# Air status label
air_status_lbl = Label(window, text="Air Status: Everything Nominal", font=('', 14))
air_status_lbl.grid(column=0, row=6)

## Column 1
# Fuel rate label
fuel_rate_lbl = Label(window, text="Fuel Rate\n.23 L/h", font=('', 32), padx=5, pady=5)
fuel_rate_lbl.grid(column=1, row=1)
# Oil temperature label
oil_temp_lbl = Label(window, text="Oil Temp.\n100 C", font=('', 24), padx=5, pady=5)
oil_temp_lbl.grid(column=1, row=2)
# Fuel level bar
fuel_lvl_bar = Progressbar(window, length=250, style='green.Horizontal.TProgressbar')
fuel_lvl_bar['value'] = 10
fuel_lvl_bar.grid(column=1, row=3)
# Fuel level label
fuel_lvl_lbl = Label(window, text="Fuel: ---%", font=('', 14))
fuel_lvl_lbl.grid(column=1, row=4)
# Fuel type label
fuel_type_lbl = Label(window, text="Fuel Type: Premium etc.", font=('', 14))
fuel_type_lbl.grid(column=1, row=5)
# Fuel status label
fuel_status_lbl = Label(window, text="Fuel Status: Everything Nominal", font=('', 14))
fuel_status_lbl.grid(column=1, row=6)