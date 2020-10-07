#!/usr/bin/python
import sys
from cx_Freeze import setup, Executable

setup(
	name = "Decrypt_Tools",
	version = "2.0",
	description = "Decrypt Your Files on the Windows",
	executables = [Executable("decryption_tool.py")]
)
