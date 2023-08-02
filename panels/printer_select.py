import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from ks_includes.screen_panel import ScreenPanel


class Panel(ScreenPanel):
    def __init__(self, screen, title):
        super().__init__(screen, title)
        printers = self._config.get_printers()

        grid = self._gtk.HomogeneousGrid()
        scroll = self._gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll.add(grid)
        self.content.add(scroll)

        length = len(printers)
        if length == 4:
            # Arrange 2 x 2
            columns = 2
        elif 4 < length <= 6:
            # Arrange 3 x 2
            columns = 3
        else:
            columns = 4

        for i, printer in enumerate(printers):
            name = list(printer)[0]
            if name == "FLSUN V400": # Changes
                self.labels[name] = self._gtk.Button("V400_thumbnail", name, f"color{1 + i % 4}", 6) # Changes
            elif name == "FLSUN SR": # Changes
                self.labels[name] = self._gtk.Button("SR_thumbnail", name, f"color{1 + i % 4}", 6) # Changes
            elif name == "FLSUN QQSP": # Changes
                self.labels[name] = self._gtk.Button("QQSP_thumbnail", name, f"color{1 + i % 4}", 6) # Changes
            elif name == "FLSUN Q5": # Changes
                self.labels[name] = self._gtk.Button("Q5_thumbnail", name, f"color{1 + i % 4}", 6) # Changes
            else: # Changes
                self.labels[name] = self._gtk.Button("printer", name, f"color{1 + i % 4}", 6) # Changes
            self.labels[name].connect("clicked", self.connect_printer, name)
            if self._screen.vertical_mode:
                row = i % columns
                col = int(i / columns)
            else:
                col = i % columns
                row = int(i / columns)
            grid.attach(self.labels[name], col, row, 1, 1)

    def connect_printer(self, widget, name):
        self._screen.connect_printer(name)

    def activate(self):
        self._screen.base_panel.action_bar.hide()
        GLib.timeout_add(0, self._screen.base_panel.action_bar.hide) # Changes
        if self._screen._ws:
            self._screen._ws.connecting = False
