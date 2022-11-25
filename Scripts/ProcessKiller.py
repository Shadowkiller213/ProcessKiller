import os
import sys
import shutil
import psutil
import time

start = time.time()

while True:
    try:
        for proc in psutil.process_iter():
            print(proc.name())
            if "roblox" in proc.name().lower():
                proc.kill()
        
        os.chdir(os.path.expandvars(r"C:\Users\\Ученик\\AppData\Roaming"))

        for x in os.listdir(os.getcwd()):
            if 'roblox' in x.lower() and os.path.isdir(x):
                shutil.rmtree(x, ignore_errors=True)

        os.chdir(os.path.expandvars(r"C:\Users\\Ученик\\AppData\Local"))
        for x in os.listdir(os.getcwd()):
            if 'roblox' in x.lower() and os.path.isdir(x):
                shutil.rmtree(x, ignore_errors=True)

        os.chdir(os.path.expandvars(r"C:\Users\\Ученик\\Downloads"))
        for x in os.listdir(os.getcwd()):
            if 'roblox' in x.lower():
                os.remove(x)
    except  Exception:
        pass

    time.sleep(0.5 * 60)
