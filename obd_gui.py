# Import base
from tkinter import *

# Imports for progress bar
from tkinter.ttk import Progressbar
from tkinter import ttk

# Create window
window = Tk()
window.title("OBD DISPLAY")
#window.geometry('800x480')
window.geometry('400x240')

# Create green progress bar style
style = ttk.Style()
style.theme_use('default')
style.configure("green.Horizontal.TProgressbar", background='green')

# MPH label
mph_lbl = Label(window, text="00 MPH", font=('', 48), padx=5, pady=5)
mph_lbl.grid(column=0, row=0)

# RPM label
rpm_lbl = Label(window, text="0000 RPM", font=('', 24), padx=5, pady=5)
rpm_lbl.grid(column=0, row=1)

# RPM bar
rpm_bar = Progressbar(window, length=200, style='green.Horizontal.TProgressbar')
rpm_bar['value'] = 1
rpm_bar.grid(column=0, row=2)

# Connection labels
conn_lbl = Label(window, text="Connecting...", font=('', 14), padx=5, pady=5)
conn_lbl.grid(column=0, row=3)