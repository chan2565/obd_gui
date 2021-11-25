from ..obd_gui import (active_shift_lbl, air_temp_lbl, base_shift_lbl,
                       coolant_temp_lbl, engine_load_lbl, mph_lbl,
                       new_coolant_temp, new_engine_load, new_intake_temp,
                       new_rpm, new_speed, new_throttle_pos, new_timing_adv,
                       rpm_bar, rpm_lbl, shift_lbl, throttle_pos_lbl,
                       timing_adv_lbl, window)


class TestRPMColors:
    def test_rpm_color(self):
        assert rpm_bar["style"] == "green.Horizontal.TProgressbar"
        assert shift_lbl["text"] == base_shift_lbl
        new_rpm("1234.567")
        assert rpm_bar["style"] == "green.Horizontal.TProgressbar"
        assert shift_lbl["text"] == base_shift_lbl
        new_rpm("4599.567")
        assert rpm_bar["style"] == "green.Horizontal.TProgressbar"
        assert shift_lbl["text"] == base_shift_lbl
        new_rpm("4600.567")
        assert rpm_bar["style"] == "red.Horizontal.TProgressbar"
        assert shift_lbl["text"] == active_shift_lbl
        new_rpm("6400.567")
        assert rpm_bar["style"] == "red.Horizontal.TProgressbar"
        assert shift_lbl["text"] == active_shift_lbl
        new_rpm("1234.567")
        assert rpm_bar["style"] == "green.Horizontal.TProgressbar"
        assert shift_lbl["text"] == base_shift_lbl

class TestCoolantColors:
    def test_coolant_temp_color(self):
        assert coolant_temp_lbl["bg"] == "black"
        new_coolant_temp("0 deg C")
        assert coolant_temp_lbl["bg"] == "yellow"
        new_coolant_temp("74 deg C")
        assert coolant_temp_lbl["bg"] == "yellow"
        new_coolant_temp("75 deg C")
        assert coolant_temp_lbl["bg"] == "green"
        new_coolant_temp("80 deg C")
        assert coolant_temp_lbl["bg"] == "green"
        new_coolant_temp("99 deg C")
        assert coolant_temp_lbl["bg"] == "green"
        new_coolant_temp("100 deg C")
        assert coolant_temp_lbl["bg"] == "red"
        new_coolant_temp("120 deg C")
        assert coolant_temp_lbl["bg"] == "red"
        new_coolant_temp("80 deg C")
        assert coolant_temp_lbl["bg"] == "green"
        new_coolant_temp("0 deg C")
        assert coolant_temp_lbl["bg"] == "yellow"

class TestEngineLoadColors:
    def test_engine_load_color(self):
        assert engine_load_lbl["fg"] == "white"
        assert engine_load_lbl["bg"] == "black"
        new_engine_load("0.0123")
        assert engine_load_lbl["fg"] == "white"
        assert engine_load_lbl["bg"] == "black"
        new_engine_load("25.0123")
        assert engine_load_lbl["fg"] == "white"
        assert engine_load_lbl["bg"] == "black"
        new_engine_load("84.0123")
        assert engine_load_lbl["fg"] == "white"
        assert engine_load_lbl["bg"] == "black"
        new_engine_load("85.0123")
        assert engine_load_lbl["fg"] == "black"
        assert engine_load_lbl["bg"] == "red"
        new_engine_load("99.0123")
        assert engine_load_lbl["fg"] == "black"
        assert engine_load_lbl["bg"] == "red"
        new_engine_load("25.0123")
        assert engine_load_lbl["fg"] == "white"
        assert engine_load_lbl["bg"] == "black"
