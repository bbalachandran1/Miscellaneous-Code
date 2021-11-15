import os
from time import *
import urllib.request

url = "https://www.google.com"

while(True):
    try:
        status_code = urllib.request.urlopen(url).getcode()
        os.system("powershell write-host -fore Green Connection Stable")
        sleep(10)
        
    except:
        os.system("netsh interface show interface")
        os.system("powershell write-host -fore Red Connection Failed. Disabling Network Adapter...")
        os.system("netsh interface set interface \"Wi-Fi\" disable")
        os.system("powershell write-host -fore Yellow Network Adapter has been disabled")
        sleep(1)
        os.system("netsh interface show interface")
        os.system("netsh interface set interface \"Wi-Fi\" enable")
        os.system("powershell write-host -fore Yellow Network Adapter has been reenabled")
        
        os.system("powershell write-host -fore Green Connection Reset")
        sleep(60)
