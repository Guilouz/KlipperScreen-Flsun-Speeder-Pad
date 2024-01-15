# KlipperScreen for FLSUN Speeder Pad

![Sans titre-2 copie](https://user-images.githubusercontent.com/12702322/196842330-e200350d-496f-4a1b-a8f7-1793d781dccb.jpg)

KlipperScreen is a touchscreen GUI that interfaces with [Klipper](https://github.com/kevinOConnor/klipper) via [Moonraker](https://github.com/arksine/moonraker). It can switch between multiple printers to access them from a single location, and it doesn't even need to run on the same host, you can install it on another device and configure the IP address to access the printer.

### Documentation [![Documentation Status](https://readthedocs.org/projects/klipperscreen/badge/?version=latest)](https://klipperscreen.readthedocs.io/en/latest/?badge=latest)

[Click here to access the documentation.](https://klipperscreen.readthedocs.io/en/latest/)

<br />

## About

This version of KlipperScreen is compatible with FLSUN Speeder Pad, it's optimized for Delta printers.

- Latest build of KlipperScreen
- Improved Z-Offset Calibration menu
- Added support for Endstops Phase Calibration
- Some fixes and adjustments

Improved Klipper Configurations are also available here : [Klipper-Flsun-Speeder-Pad](https://github.com/Guilouz/Klipper-Flsun-Speeder-Pad)

<br />

If you like my work, don't hesitate to support me by paying me a 🍺 or a ☕. Thank you 🙂

[ ![Donate](https://github-production-user-asset-6210df.s3.amazonaws.com/12702322/259218308-192804d4-cb79-44cd-a9a9-d90664e03076.png) ](https://ko-fi.com/guilouz)

<br />

## Installation

- Make sure previous installation of KlipperScreen is removed (with Kiauh).
- In SSH, enter the following commands (one at a time) to install KlipperScreen:
```
cd ~ && git clone https://github.com/Guilouz/KlipperScreen-Flsun-Speeder-Pad.git
```
```
sudo mv ~/KlipperScreen-Flsun-Speeder-Pad ~/KlipperScreen
```
```
./KlipperScreen/scripts/KlipperScreen-install-fix.sh
```

- Go to your Mainsail Web interface then select the `Machine` tab.
- Open the `moonraker.conf` file and modify the `[update_manager KlipperScreen]` section  as follows:

```
[update_manager KlipperScreen]
type: git_repo
path: ~/KlipperScreen
origin: https://github.com/Guilouz/KlipperScreen-Flsun-Speeder-Pad.git
virtualenv: ~/.KlipperScreen-env
requirements: scripts/KlipperScreen-requirements.txt
system_dependencies: scripts/system-dependencies.json
managed_services: KlipperScreen
```
- Once done, click on `SAVE & RESTART` at the top right to save the file.
- You can now click the refresh button (still in the Machine tab) on the `Update Manager` tile.
- You will see a new KlipperScreen update appear, if you see a ⚠️DIRTY update, just select `Hard Recovery` to update.

![Update Manager](https://user-images.githubusercontent.com/12702322/183909392-24aab778-c8ed-4f81-be39-ac51612bf12c.jpg)

- Once installed you will have the new version of KlipperScreen and future updates will point directly to my repo like this:

![Update](https://user-images.githubusercontent.com/12702322/183990132-0a7673d1-2e51-484a-8113-e0bd54813995.jpg)

<br />

## Restoration

- Make sure previous installation of KlipperScreen is removed (with Kiauh).
- In SSH, enter the following commands (one at a time) to install KlipperScreen:
```
cd ~ && git clone https://github.com/KlipperScreen/KlipperScreen.git
```
```
./KlipperScreen/scripts/KlipperScreen-install.sh
```
Note: Installation may take several minutes.

- Go to your Mainsail Web interface then select the `Machine` tab.
- Open the `moonraker.conf` file and modify the `[update_manager KlipperScreen]` section  as follows:

```
[update_manager KlipperScreen]
type: git_repo
path: ~/KlipperScreen
origin: https://github.com/KlipperScreen/KlipperScreen.git
virtualenv: ~/.KlipperScreen-env
requirements: scripts/KlipperScreen-requirements.txt
system_dependencies: scripts/system-dependencies.json
managed_services: KlipperScreen
```

<br />

## Notes

- This version of KlipperScreen use the following Macros:

  - `Z Offset Calibration` function use `[gcode_macro Z_OFFSET_CALIBRATION]`
  - `EndStops Calibration` function use `[gcode_macro ENDSTOPS_CALIBRATION]`
  - `Automatic Delta Calibration` function use `[gcode_macro DELTA_CALIBRATION]`
  - `Apply a safety Offset` function use `[gcode_macro SECURITY_OFFSET]`
  - `Bed Mesh` function use `[gcode_macro BED_LEVELING]`
  - `Hotend PID` function use `[gcode_macro PID_HOTEND]`
  - `Bed PID` function use `[gcode_macro PID_BED]`
  - `Hotend LED Off` function use `[gcode_macro LED_HOTEND_OFF]`
  - `Hotend LED On` function use `[gcode_macro LED_HOTEND_ON]`
  - `Logo LED Off` function use `[gcode_macro LED_LOGO_OFF]`
  - `Logo LED On` function use `[gcode_macro LED_LOGO_ON]`

<br />

- To use `M600` Macro, you need to change `[filament_switch_sensor filament_sensor]` section in your `printer.cfg` file like this:
```
[filament_switch_sensor filament_sensor]
pause_on_runout: True
runout_gcode: M600
...
```

<br />

- To have screen notifications, add this in your `printer.cfg` file:
```
[respond]
```

<br />

- To use Endstops Calibrate function, it's needed to have this in your `printer.cfg` file:
```
[endstop_phase stepper_a]
endstop_align_zero: false

[endstop_phase stepper_b]
endstop_align_zero: false

[endstop_phase stepper_c]
endstop_align_zero: false
```

<br />

- This version of KlipperScreen save Z-Offset in real time. This is needed:

- Add this in your `printer.cfg` file:
```
[save_variables]
filename: ~/printer_data/config/variables.cfg
```
- And must be used with this Macros:
```
[gcode_macro SET_GCODE_OFFSET]
description: Saving Z-Offset
rename_existing: _SET_GCODE_OFFSET
gcode:
  {% if printer.save_variables.variables.gcode_offsets %}
  {% set offsets = printer.save_variables.variables.gcode_offsets %}
  {% else %}
  {% set offsets = {'z': None} %}
  {% endif %}
  {% set ns = namespace(offsets={'z': offsets.z}) %}
  _SET_GCODE_OFFSET {% for p in params %}{'%s=%s '% (p, params[p])}{% endfor %}
  {%if 'Z' in params %}{% set null = ns.offsets.update({'z': params.Z}) %}{% endif %}
  {%if 'Z_ADJUST' in params %}
  {%if ns.offsets.z == None %}{% set null = ns.offsets.update({'z': 0}) %}{% endif %}
  {% set null = ns.offsets.update({'z': (ns.offsets.z | float) + (params.Z_ADJUST | float)}) %}
  {% endif %}
  SAVE_VARIABLE VARIABLE=gcode_offsets VALUE="{ns.offsets}"
```
```
[delayed_gcode LOAD_GCODE_OFFSETS]
initial_duration: 2
gcode:
  {% if printer.save_variables.variables.gcode_offsets %}
  {% set offsets = printer.save_variables.variables.gcode_offsets %}
  _SET_GCODE_OFFSET {% for axis, offset in offsets.items() if offsets[axis] %}{ "%s=%s " % (axis, offset) }{% endfor %}
  { action_respond_info("Loaded Z-Offset from variables.cfg file: %s" % (offsets)) }
  {% endif %}
```

<br />

- To display printers icons on printer select screen, your printers must be named like that:
  - Flsun V400: `FLSUN V400`
  - Flsun Super Racer: `FLSUN SR`
  - Flsun QQS Pro: `FLSUN QQSP`
  - Flsun Q5: `FLSUN Q5`

<br />

## Changelog

Changelog is available here: https://github.com/Guilouz/Klipper-Flsun-Speeder-Pad/wiki/KlipperScreen-Changelog
