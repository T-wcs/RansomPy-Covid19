#!/usr/bin/python
import struct, ctypes, os, shutil, sys

def copy_img():
    path = os.getcwd()
    img = "\\setup\\image.jpg"
    Wallpaper = "%s%s" %(path, img)
    filePath = shutil.copy(Wallpaper, '\\PerfLogs\\image.jpg')

def is_64_windows():
    # Find out how many bits is OS
    return struct.calcsize('P') * 8 == 64

def get_sys_parameters_info():
    # Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA

def change_wallpaper():
    try:
        SPI_SETDESKWALLPAPER = 20
        WALLPAPER_PATH = "\\PerfLogs\\image.jpg"
        sys_parameters_info = get_sys_parameters_info()
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
        if not r:
            print(ctypes.WinError())
    except:
        pass
