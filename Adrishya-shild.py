import subprocess
import time
import sys
import os

class colors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(colors.OKBLUE,colors.BOLD,"""
 
░█████╗░██████╗░██████╗░██╗░██████╗██╗░░██╗██╗░░░██╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║░░██║╚██╗░██╔╝██╔══██╗
███████║██║░░██║██████╔╝██║╚█████╗░███████║░╚████╔╝░███████║
██╔══██║██║░░██║██╔══██╗██║░╚═══██╗██╔══██║░░╚██╔╝░░██╔══██║
██║░░██║██████╔╝██║░░██║██║██████╔╝██║░░██║░░░██║░░░██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

███████████████████████████
█─▄▄▄▄█─█─█▄─▄█▄─▄███▄─▄▄▀█
█▄▄▄▄─█─▄─██─███─██▀██─██─█
▀▄▄▄▄▄▀▄▀▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀

                                                @kartikhunt3r


""",colors.ENDC)




if os.name!='nt':


    print(colors.OKGREEN,colors.BOLD,"Scanning For Harmful Files:")


    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■□□□□□□]","[■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.6)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

    subprocess.call("rm -r /root/.sysconfig", shell=True)

    print(colors.FAIL,colors.BOLD,"Removing Keyloggers:")


    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■□□□□□□]","[■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.10)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

    subprocess.call("rm ~/.config/autostart/sysconfig.desktop", shell=True)

    print(colors.OKBLUE,colors.BOLD,"Reconfiguring System Files:")


    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■□□□□□□]","[■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.4)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

    time.sleep(1)

    print(colors.OKGREEN,colors.BOLD,"[+]Congratulations!! Keylogger Removed Successfully")
    print("\n")
    subprocess.call("pkill -9 python3", shell=True)

else:

    print(colors.OKGREEN,colors.BOLD,"Scanning For Harmful Files:")


    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■□□□□□□]","[■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.6)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

    subprocess.call("start /b reg DELETE HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /f", shell=True)

    print(colors.FAIL,colors.BOLD,"Removing Keyloggers:")


    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■□□□□□□]","[■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.10)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

    subprocess.call('rmdir "C:\System36"', shell=True)

    print(colors.OKBLUE,colors.BOLD,"Reconfiguring System Files:")


    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■□□□□□□]","[■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.4)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

    time.sleep(1)

    print(colors.OKGREEN,colors.BOLD,"[+]Congratulations!! Keylogger Removed Successfully")
    print("\n")
    subprocess.call("taskkill /IM python.exe /F", shell=True)
