# Changes Start
import gi
import logging
import re

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from ks_includes.KlippyGcodes import KlippyGcodes
from ks_includes.screen_panel import ScreenPanel

def create_panel(*args):
    return ZCalibratePanel(*args)

class ZCalibratePanel(ScreenPanel):
    user_selecting = False

    bs = 0
    bs_delta = "0.1"
    bs_deltas = ["0.01", "0.05", "0.1", "0.5", "1"]

    def initialize(self, panel_name):

        logging.debug("ZCalibratePanel")

        grid = self._gtk.HomogeneousGrid()
        grid.set_row_homogeneous(False)
        self.labels['start'] = self._gtk.ButtonImage('arrow-down', _("Move Z0"), 'color1')
        script = {"script": "MOVE_TO_Z0"}
        self.labels['start'].connect("clicked", self._screen._confirm_send_action,
                                          _("Please remove leveling switch before move Z0."),
                                          "printer.gcode.script", script)
        self.labels['home'] = self._gtk.ButtonImage("home", _("Home"), "color1")
        self.labels['home'].connect("clicked", self.go_to_home, "home")
        self.labels['z+'] = self._gtk.ButtonImage("z-farther", _("Raise Nozzle"), "color1")  
        self.labels['z+'].connect("clicked", self.change_babystepping, "+")
        self.labels['zoffset'] = Gtk.Label("0.00" + _("mm"))         
        self.labels['z-'] = self._gtk.ButtonImage("z-closer", _("Lower Nozzle"), "color1")
        self.labels['z-'].connect("clicked", self.change_babystepping, "-")
        self.labels['move_dist'] = Gtk.Label(_("Move Distance (mm)"))
        self.labels['blank'] = Gtk.Label()
        
        grid.attach(self.labels['start'], 0, 0, 1, 1)
        grid.attach(self.labels['home'], 0, 1, 1, 1)
        grid.attach(self.labels['z+'], 1, 0, 2, 1)
        grid.attach(self.labels['z-'],  1, 1, 2, 1)
        grid.attach(self.labels['blank'], 0, 3, 1, 1)
        grid.attach(self.labels['zoffset'], 0, 4, 1, 1)
        grid.attach(self.labels['move_dist'], 0, 5, 1, 1)

        bsgrid = Gtk.Grid()
        j = 0
        for i in self.bs_deltas:
            self.labels[i] = self._gtk.ToggleButton(i)
            self.labels[i].connect("clicked", self.change_bs_delta, i)
            ctx = self.labels[i].get_style_context()
            if j == 0:
                ctx.add_class("distbutton_top")
            elif j == len(self.bs_deltas)-1:
                ctx.add_class("distbutton_bottom")
            else:
                ctx.add_class("distbutton")
            if i == self.bs_delta:
                ctx.add_class("distbutton_active")
            bsgrid.attach(self.labels[i], j, 0, 1, 1)
            j += 1
        grid.attach(bsgrid, 1, 5, 2, 1)

        self.content.add(grid)

    def process_update(self, action, data):

        if action != "notify_status_update":
            return

        if "gcode_move" in data:
            if "homing_origin" in data["gcode_move"]:
                self.labels['zoffset'].set_text("Z Offset: %.2fmm" % data["gcode_move"]["homing_origin"][2])

    def change_babystepping(self, widget, dir):
        if dir == "+":
            gcode = "SET_GCODE_OFFSET Z_ADJUST=%s MOVE=1" % self.bs_delta
        else:
            gcode = "SET_GCODE_OFFSET Z_ADJUST=-%s MOVE=1" % self.bs_delta

        self._screen._ws.klippy.gcode_script(gcode)

    def go_to_home(self, widget, home):
        gcode = "LED_HOTEND_OFF\nG28"

        self._screen._ws.klippy.gcode_script(gcode)

    def change_bs_delta(self, widget, bs):
        if self.bs_delta == bs:
            return
        logging.info("### BabyStepping " + str(bs))

        ctx = self.labels[str(self.bs_delta)].get_style_context()
        ctx.remove_class("distbutton_active")

        self.bs_delta = bs
        ctx = self.labels[self.bs_delta].get_style_context()
        ctx.add_class("distbutton_active")
        for i in self.bs_deltas:
            if i == self.bs_delta:
                continue
            self.labels[i].set_active(False)
# Changes End
