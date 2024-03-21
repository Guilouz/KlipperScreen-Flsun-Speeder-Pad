import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from ks_includes.screen_panel import ScreenPanel
from ks_includes.widgets.autogrid import AutoGrid


class Panel(ScreenPanel):
    def __init__(self, screen, title):
        super().__init__(screen, title)
        printers = self._config.get_printers()

        printer_buttons = []
        for i, printer in enumerate(printers):
            name = list(printer)[0]
            #self.labels[name] = self._gtk.Button("extruder", name, f"color{1 + i % 4}") # Changes
            # Start Changes
            if name == "FLSUN V400":
                self.labels[name] = self._gtk.Button("V400_thumbnail", name, f"color{1 + i % 4}", 6)
            elif name == "FLSUN SR":
                self.labels[name] = self._gtk.Button("SR_thumbnail", name, f"color{1 + i % 4}", 6)
            elif name == "FLSUN QQSP":
                self.labels[name] = self._gtk.Button("QQSP_thumbnail", name, f"color{1 + i % 4}", 6)
            elif name == "FLSUN Q5":
                self.labels[name] = self._gtk.Button("Q5_thumbnail", name, f"color{1 + i % 4}", 6)
            else:
                self.labels[name] = self._gtk.Button("printer", name, f"color{1 + i % 4}", 6)
            # End Changes
            self.labels[name].connect("clicked", self.connect_printer, name)
            printer_buttons.append(self.labels[name])
        grid = AutoGrid(printer_buttons, vertical=self._screen.vertical_mode)

        scroll = self._gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll.add(grid)
        self.content.add(scroll)

    def connect_printer(self, widget, name):
        self._screen.connect_printer(name)

    def activate(self):
        self._screen.base_panel.action_bar.hide()
        #GLib.timeout_add(100, self._screen.base_panel.action_bar.hide) # Changes
        GLib.timeout_add(0, self._screen.base_panel.action_bar.hide) # Changes
        if self._screen._ws:
            self._screen._ws.connecting = False
