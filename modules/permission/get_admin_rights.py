#!/usr/bin/python
#coding:utf-8
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("You program Here if the program run with Admin permission")
else:
    print("Or restart the program with Admin permission")
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)

"""
Si vous souhaité convertir le script python dans un fichier exécutable
(en utilisant des outils tels que py2exe, cx_freeze, pyinstaller)
alors utiliser sys.argv[1:] au lieu de sys.argv pour le quatrième paramètre.
"""
"""
If you want to convert the python script into an executable file
(using tools such as py2exe, cx_freeze, pyinstaller)
then use sys.argv[1:] instead of sys.argv for the fourth parameter.
"""
