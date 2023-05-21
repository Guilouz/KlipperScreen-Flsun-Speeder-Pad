import logging

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

from ks_includes.KlippyGcodes import KlippyGcodes
from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return PidPanel(*args)


class PidPanel(ScreenPanel):

    def __init__(self, screen, title):
        super().__init__(screen, title)
        macros = self._printer.get_gcode_macros()
        self.hotend_pid = any("PID_HOTEND" in macro.upper() for macro in macros)
        self.bed_pid = any("PID_BED" in macro.upper() for macro in macros)
        self.buttons = {
            'hotend': self._gtk.Button("extruder", _("Hotend PID"), "color1"),
            'bed': self._gtk.Button("bed", _("Bed PID"), "color1"),
        }

        self.buttons['hotend'].connect("clicked", self.start_hotend_pid)
        self.buttons['bed'].connect("clicked", self.start_bed_pid)

        grid = self._gtk.HomogeneousGrid()
        grid.attach(self.buttons['hotend'], 0, 0, 1, 1)
        grid.attach(self.buttons['bed'], 1, 0, 1, 1)

        self.content.add(grid)

    def start_hotend_pid(self, widget):
        if not self.hotend_pid:
            self._screen.show_popup_message("Macro PID_HOTEND" + _("not found!\nPlease update your configuration files."))
        else:
            script = {"script": "PID_HOTEND"}
            self._screen._confirm_send_action(None, _("Do you want to start PID calibration for Hotend?"), "printer.gcode.script", script)

    def start_bed_pid(self, widget):
        if not self.bed_pid:
            self._screen.show_popup_message("Macro PID_BED" + _("not found!\nPlease update your configuration files."))
        else:
            script = {"script": "PID_BED"}
            self._screen._confirm_send_action(None, _("Do you want to start PID calibration for Bed?"), "printer.gcode.script", script)

    def process_busy(self, busy):
        buttons = ("hotend", "bed")
        for button in self.buttons:
            self.buttons[button].set_sensitive(not busy)

    def process_update(self, action, data):
        if action == "notify_busy":
            self.process_busy(data)
            return
        elif action == "notify_gcode_response":
            data = data.lower()
            if "unknown" in data:
                self.buttons['hotend'].set_sensitive(False)
                self.buttons['pid'].set_sensitive(False)
                logging.info(data)
            elif "save_config" in data:
                self.buttons['hotend'].set_sensitive(False)
                self.buttons['pid'].set_sensitive(False)
            elif "out of range" in data:
                self._screen.show_popup_message(data)
                self.buttons['hotend'].set_sensitive(False)
                self.buttons['pid'].set_sensitive(False)
                logging.info(data)
        return
