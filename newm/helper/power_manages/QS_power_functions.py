from __future__ import annotations
from typing import TypeVar, Optional, Callable, Any, Generic, Union, cast
#imports
import os
import subprocess
import pathlib
import importlib
import sys
#home_directory, and import manage_energy configuration
module_path = "~/.config/newm"
module_path = os.path.expanduser(module_path)

path_file = os.path.expanduser("~/.config/newm/QS_power.py")
if os.path.exists(path_file):
    sys.path.append(module_path)
    import QS_power
    energy = QS_power.energy
else:
    path_file = os.path.expanduser("/etc/newm/QS_power.py")
    module_path = "/etc/newm/"
    module_path = os.path.expanduser(module_path)
    if os.path.exists(path_file):
        sys.path.append(module_path)
        import QS_power
        energy = QS_power.energy
    else:
        from newm import QS_power_default
        energy = QS_power_default.energy
#variables
QS_light_score = 0
QS_current_light = 0
power_check = {}
display_off = "brightnessctl set 0"
lock_screen = "newm-cmd lock config=dim"
suspend = "systemctl suspend &"
hibernate = "systemctl hibernate &"
#The function of determining the current brightness of the screen
def checked_current_brightness():
    QS_light_result = subprocess.run(["brightnessctl", "g"], stdout=subprocess.PIPE, text=True)
    QS_current_brightness = int(QS_light_result.stdout.strip())
    return QS_current_brightness
