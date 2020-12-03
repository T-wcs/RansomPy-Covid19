#!/usr/bin/python
#coding:utf-8
import os, sys, ctypes, shutil, time
# ENVIRONMENT VARIABLE
usr = os.environ["USERNAME"]
d = os.environ["SystemDrive"]

class CopyGui():
    """ Classe qui permet de copier l'ensemble du répertoire du Compteur """
    def __init__(self):
        self.prf = "\\PerfLogs\\setup"
    # COPY TO GUI COUNTER DIRECTORY TEMP
    def cp_guitmp(self):
        try:
            cpath = os.getcwd()
            src_tmp = "{}\\setup".format(cpath)
            dst_tmp = "{}".format(self.prf)
            cpy = shutil.copytree(src_tmp, dst_tmp)
        except:
            pass
    def cp_gui(self):
        try:
            src = "{}".format(self.prf)
            dst = "{}\\Users\\{}\\AppData\\setup".format(d, usr)
            cpy = shutil.copytree(src, dst)
        except:
            pass
