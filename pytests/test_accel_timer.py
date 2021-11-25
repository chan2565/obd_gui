from time import sleep
from ..obd_gui import (accel_lbl, active_shift_lbl, air_temp_lbl,
                       base_accel_lbl, base_shift_lbl, coolant_temp_lbl,
                       engine_load_lbl, mph_lbl, new_coolant_temp,
                       new_engine_load, new_intake_temp, new_rpm, new_speed,
                       new_throttle_pos, new_timing_adv, rpm_bar, rpm_lbl,
                       shift_lbl, throttle_pos_lbl, timing_adv_lbl, window)

class TestAccelTimer:
    def test_accel_timer(self):
        speed = 0.0

        # Stopping short of 60 mph
        while speed < 60.0:
            new_speed(str(speed) + " kph")
            speed = speed + 1.0
            sleep(.01)
        while speed >= 0.0:
            new_speed(str(speed) + " kph")
            speed = speed - 1.0
            sleep(.01)
        assert "----" in accel_lbl["text"]

        # Changing speed while stopping short of 60 mph
        while speed < 60.0:
            new_speed(str(speed) + " kph")
            speed = speed + 1.0
            sleep(.01)
        while speed > 30.0:
            new_speed(str(speed) + " kph")
            speed = speed - 1.0
            sleep(.01)
        while speed < 60.0:
            new_speed(str(speed) + " kph")
            speed = speed + 1.0
            sleep(.01)
        while speed >= 0.0:
            new_speed(str(speed) + " kph")
            speed = speed - 1.0
            sleep(.01)
        assert "----" in accel_lbl["text"]

        # Full 0-60 mph run from a stop
        while speed < 120.0:
            new_speed(str(speed) + " kph")
            speed = speed + 1.0
            sleep(.01)
        while speed >= 0.0:
            new_speed(str(speed) + " kph")
            speed = speed - 1.0
            sleep(.01)
        assert "----" not in accel_lbl["text"]
