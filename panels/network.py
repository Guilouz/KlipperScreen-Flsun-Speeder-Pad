# Pick the network panel backend at load time:
# - NetworkManager running -> panel based on sdbus-networkmanager
# - otherwise (e.g. stock Speeder Pad image) -> panel based on wpa_supplicant
import os

if os.system('systemctl is-active --quiet NetworkManager.service') == 0:
    from panels.network_nm import Panel  # noqa: F401
else:
    from panels.network_wpa import Panel  # noqa: F401
