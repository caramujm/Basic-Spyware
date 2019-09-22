# Basic-Spyware

-> Written in:
Python3


-> How the program works:
The target are home PCs owned by people that are trying to get a paid software for free.
The program is divided into two pieces the Crack.exe and the WindowsAlert.exe.
Crack.exe will run, move the WindoesAlert.exe to a new dir, add to Registry to run the program in the Startup and add host entries to give a perception that actually worked (block ads).
Crack.exe can be modified to combine with the targed software that you want to send to the victim.
WindowsAlert.exe is a keylogger that will send to your email a .txt where all keyboard inputs of the victim will be written.
Note: WindowsAlert.exe in my case is in a subdir existed in the Spotify dir.


-> My finally test:
In the example the software that I used to be cracked was Spotify.
To persuade the victims, I used pyinstaller to transform into an exe file.                                     
https://datatofish.com/executable-pyinstaller/ >pyinstaller --onefile pythonScriptName.py                                                  
Resource Hacker was used to give the .exe an icon.
http://www.angusj.com/resourcehacker/


-> Virus Total:
https://imgur.com/a/UWdbBfS


-> What can be improved:
Add more docstrings and documentation.


-> Why was created for:
Learn more about python and windows. I tested on myself and was not created for bad purposes.
