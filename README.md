# KlipperScreen for FLSUN V400

![test-flsun-v400 jpg 3683ed2615cedff6a17e282b2dc48190 thumb jpg c579e0706751042e9e214feb12a7c162](https://user-images.githubusercontent.com/12702322/183767560-330689f3-61f6-42d3-9daf-b6c3e6ff845a.jpg)

KlipperScreen is a touchscreen GUI that interfaces with [Klipper](https://github.com/kevinOConnor/klipper) via [Moonraker](https://github.com/arksine/moonraker). It can switch between multiple printers to access them from a single location, and it doesn't even need to run on the same host, you can install it on another device and configure the IP address to access the printer.

### Documentation [![Documentation Status](https://readthedocs.org/projects/klipperscreen/badge/?version=latest)](https://klipperscreen.readthedocs.io/en/latest/?badge=latest)

[Click here to access the documentation.](https://klipperscreen.readthedocs.io/en/latest/)

## About

This version of KlipperScreen is compatible with FLSUN's Speeder Pad, it's optimized for Delta printers.

- Latest build of KlipperScreen
- Improved Z-Offset Calibration menu
- Added support for Endstops Phase Calibration
- Some fixes and adjustments

Improved Klipper Configuration for V400 is also available here : [Klipper-Flsun-V400](https://github.com/Guilouz/Klipper-Flsun-V400)

<br />

If you like my work, don't hesitate to support me by paying me a 🍺 or a ☕. Thank you 🙂

[ ![Download](https://user-images.githubusercontent.com/12702322/115148445-e5a40100-a05f-11eb-8552-c1f5d4355987.png) ](https://www.paypal.me/CyrilGuislain)


## Installation

- Go to your Mainsail Web interface then select the `Machine` tab.
- Right-click on the `moonraker.conf` file then `Download` to make a backup of the original file. Keep this file carefully for possible backtracking.
- Now, still on Mainsail, open the `moonraker.conf` file and modify the `[update_manager KlipperScreen]` section  as follows:

```
[update_manager KlipperScreen]
type: git_repo
path: /home/pi/KlipperScreen
origin: https://github.com/Guilouz/KlipperScreen-Flsun-V400.git
env: /home/pi/.KlipperScreen-env/bin/python
requirements: scripts/KlipperScreen-requirements.txt
install_script: scripts/KlipperScreen-install.sh
```
- Once done, click on `Save & close` at the top right to save the file.
- You can now click the refresh button (still in the Machine tab) on the `Update Manager` tile.
- You will see a new KlipperScreen update appear, if you see a ⚠️DIRTY update, just select `Hard Recovery` to update.

![Update Manager](https://user-images.githubusercontent.com/12702322/183909392-24aab778-c8ed-4f81-be39-ac51612bf12c.jpg)

- Once installed you will have the new version of KlipperScreen and future updates will point directly to my repo like this:

![Update](https://user-images.githubusercontent.com/12702322/183990132-0a7673d1-2e51-484a-8113-e0bd54813995.jpg)


## Restoration

- If you want to go back to the Flsun version, you can simply restore the previously downloaded `moonraker.conf` file or re-edit the `[update_manager KlipperScreen]` section and click the refresh button on the `Update Manager` tile:

```
[update_manager KlipperScreen]
type: git_repo
path: /home/pi/KlipperScreen
origin: https://gitee.com/zzcatvs/KlipperScreen.git
env: /home/pi/.KlipperScreen-env/bin/python
requirements: scripts/KlipperScreen-requirements.txt
install_script: scripts/KlipperScreen-install.sh
```

## Changelog

- 28/08/2022 : Latest KlipperScreen commits / Power on Hotend LED when calibrate Z-Offset
- 17/08/2022 : Added Home button in Z Calibrate menu / Translate Input Shaper menu / Improvements
- 16/08/2022 : Improved moves speeds / Improved French translation
- 14/08/2022 : Improved extrude/retract speeds / Improved French translation
- 13/08/2022 : Latest KlipperScreen commits
- 10/08/2022 : First release
