import os
import time
import ctypes
import shutil
import subprocess
from pymem import Pymem


# Check if program is running as admin
if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    print("This program requires administrator to remove malicious code from system root directory. Please run as admin.")
    time.sleep(5)
    exit()



# Check if program will run correctly on this machine
control = os.popen('pip list | findstr os').read()
if not control:
    print("Something went wrong...")
    time.sleep(3)
    exit()




pkg1 = os.popen('pip list | findstr adm4').read() # Active package
pkg2 = os.popen('pip list | findstr admcheck').read() # Banned package




def isRunning():
    try:
        Pymem('server.exe')
        return True
    except:
        return False

def terminate(ProcessName):
    os.system('taskkill /im ' + ProcessName)

def writeDummy(): # Write a blank exe file
    print("Preparing to write dummy file...")
    isExist = os.path.exists("C:/Kingston")
    if not isExist:
        os.makedirs("C:/Kingston")
    with open('C:/Kingston/server.txt', 'w') as f:
        f.write('Exterminated')
    os.replace('C:\Kingston\server.txt', 'C:\Kingston\server.exe')

def patchScript():
    print("Preparing to patch malicious installer...")
    pkgloc = os.popen("python -m site | findstr \\site-packages' | findstr Local").read()
    if not pkgloc:
        print("Something went wrong finding module location...")
        time.sleep(3)
        exit()
    pkgloc = pkgloc.replace("\\\\", "/").replace("'", "").replace(",", "").replace("\n", "").replace(" ", "")
    shutil.copyfile('./Patch/dummy.py', f'{pkgloc}/adm4/main.py') #copy src to dst
    shutil.copyfile('./Patch/dummy.cpython-310.pyc', f'{pkgloc}/adm4/__pycache__/main.cpython-310.pyc') #copy src to dst

def end():
    print("\nDone.")
    print("\nThe package is installed on your system, but is now patched and harmless.")
    print("\nIt is recommended you do not uninstall the package as accidental re-installation will not include the patch.")
    time.sleep(7)
    exit()

# Exterminate
def exterminate(type):
    if type == 1: # Package already installed
        if os.path.exists("C:\Kingston\server.exe"):
            print("Malicious file exists.")
            if isRunning() == True:
                print("Malicious file is running. Terminating...")
                terminate('server.exe')
                print("Malicious file terminated.")
            else:
                print("Malicious file is not currently running.")
            print("Removing malicious file...")
            os.remove("C:\Kingston\server.exe")
            print("Malicious file removed.")
            writeDummy()
            end()
        else:
            print("The malicious file does not exist for some reason.")
            writeDummy()
            end()
    if type == 2: # Prevent future installation
        if os.path.exists("C:\Kingston\server.exe"):
            print("Malicious package has previously been installed.")
            if isRunning() == True:
                print("Malicious file is running. Terminating...")
                terminate('server.exe')
                print("Malicious file terminated.")
            else:
                print("Malicious file is not currently running.")
            print("Removing malicious file...")
            os.remove("C:\Kingston\server.exe")
            print("Malicious file removed.")

        print("Preparing to install and patch malicious package to prevent future harm...")
        subprocess.run("pip install adm4", capture_output=True)
        print("Malicious package temporarily installed.")
        patchScript()
        print("Malicious package has been patched.")
        writeDummy()
        end()




if pkg1 or pkg2:
    print("1 or more malicious packages are installed. Preparing to exterminate...")
    exterminate(1)
else:
    print("No malicious packages found on your device. Would you like to prevent future installation? (recommended)")
    inp = input("Y/n: ")
    if inp.lower() == "n":
        print("Exiting...")
        time.sleep(3)
        exit()
    if inp.lower() == "y":
        print("Preparing to prevent future installation...")
        exterminate(2)
    else:
        print("Invalid input, exiting...")
        time.sleep(3)
        exit()