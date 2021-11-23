from ..obd_gui import window, base_shift_lbl, active_shift_lbl, rpm_bar, rpm_lbl, mph_lbl, coolant_temp_lbl, air_temp_lbl, shift_lbl, engine_load_lbl, timing_adv_lbl, throttle_pos_lbl, new_coolant_temp, new_engine_load, new_intake_temp, new_rpm, new_speed, new_throttle_pos, new_timing_adv

class TestColors:
    def test_rpm_color(self):
        assert rpm_bar["style"] == "green.Horizontal.TProgressbar"