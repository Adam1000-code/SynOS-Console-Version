import os
import sys
import time
from time import sleep
from cryptography.fernet import Fernet
from random import randint

#this main file acts as a boot up sequence

system_path = "SynOS"

user_data = "username.txt"

user_data_path = "users_data"

user_store = os.path.join(system_path, user_data_path, user_data)

total_iterations = 100

def progress_bar(iteration, total, prefix="", suffix="", length=50, print_end="\r"):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = "#" * filled_length + "-" * (length - filled_length)
    sys.stdout.write(f"\r{prefix} [{bar}] {percent}% {suffix}",)
    sys.stdout.flush()
    if iteration == total:
        print(print_end)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

print("░██████╗██╗░░░██╗███╗░░██╗░█████╗░░██████╗\n██╔════╝╚██╗░██╔╝████╗░██║██╔══██╗██╔════╝\n╚█████╗░░╚████╔╝░██╔██╗██║██║░░██║╚█████╗░\n░╚═══██╗░░╚██╔╝░░██║╚████║██║░░██║░╚═══██╗\n██████╔╝░░░██║░░░██║░╚███║╚█████╔╝██████╔╝\n╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝░╚════╝░╚═════╝░")
sleep(0.7)
print("Booting...")

for i in range(total_iterations + 1):
    sleep(0.02)
    progress_bar(i, total_iterations, prefix="Progress", suffix="Complete", length=50)

sleep(0.7)

if not os.path.exists(system_path) and not os.path.exists(user_store):
    print("ERROR: system or user data missing")
    sleep(1)
    print("running installer...")
    sleep(2)
    os.system("python3 setup/install.py")
#elif os.path.exists(system_path) and os.path.exists(user_data_path):
#    os.system("python3 OS.py")
else:
    os.system("python3 OS.py")