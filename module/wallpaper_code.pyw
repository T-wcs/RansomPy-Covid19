#!/usr/bin/python
import struct, ctypes, os

# Répertoire courant
path = os.getcwd()

# wallpaper set to desktop
SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = 'PATH_TO_IMAGE_LOCATION'

Wallpaper = "%s%s" %(path, WALLPAPER_PATH)

def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, Wallpaper, 3)

    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())


change_wallpaper()
