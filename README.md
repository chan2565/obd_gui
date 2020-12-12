# OBD GUI (OG)

This is a GUI (built from [Tk](https://wiki.python.org/moin/TkInter)) for displaying OBD information from a vehicle (using the [obd](https://pypi.org/project/obd/) Python library). It is designed to be run at boot on a Raspberry Pi installed in a touchscreen case. Using a bluetooth ELM327 adapter is possible, but I've had mixed results from it, especially with connecting automatically at boot. The USB cable version is much more reliable, but you have to route the cable appropriately.

obd_gui.py  == Keep all of the GUI elements here, along with callback functions for the OBD input.
start_og.py == Sets up OBD data callbacks and starts the GUI window.

### Parts List
- Raspberry Pi (3B+ or 4)
- [SmartiPi Touch 2 Case](https://www.amazon.com/SmartiPi-Touch-Official-Raspberry-Touchscreen/dp/B07WXK38YM/)
- [ELM327 OBD USB Cable](https://www.amazon.com/Scanner-FORScan-Adapter-ELMconfig-Diagnosis/dp/B083FML519/) or similar
- MicroSD Card ([Flashed with the latest Raspbian](https://www.raspberrypi.org/software/operating-systems/))

I used [this Instructable](https://www.instructables.com/OBD-Pi/) as a starting point.