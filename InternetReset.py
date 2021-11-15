#This code was created for my roommate, Neil, to help him automatically reset the connection to his desktop
#whenever he loses connection (which often happens). My first endeavor with powershell too!

import os
from time import *
import urllib.request

#sample URL to test connection
url = "https://www.google.com"

while(True):
    #tries to navigate to google every 10 seconds, and if successful echoes Connection Stable to the Command Line
    try:
        status_code = urllib.request.urlopen(url).getcode()
        os.system("powershell write-host -fore Green Connection Stable")
        sleep(10)
       
    #resets the network adapter
    except:
        #disables the network adapter and displays Error Messages indicating the operations
        os.system("netsh interface show interface")
        os.system("powershell write-host -fore Red Connection Failed. Disabling Network Adapter...")
        os.system("netsh interface set interface \"Wi-Fi\" disable")
        os.system("powershell write-host -fore Yellow Network Adapter has been disabled")
        
        #reenables the network adapter after 1 second and echoes the output to command line
        sleep(1)
        os.system("netsh interface show interface")
        os.system("netsh interface set interface \"Wi-Fi\" enable")
        os.system("powershell write-host -fore Yellow Network Adapter has been reenabled")
        
        os.system("powershell write-host -fore Green Connection Reset")
        
        sleep(60)
