import os
import sys
import time
from time import sleep
from cryptography.fernet import Fernet
from random import randint

system_path = "SynOS"

user_data = "username.txt"

password_data = "password.txt"

key = Fernet.generate_key()

user_data_path = os.path.join(system_path, "users_data")

user_keys_path = os.path.join(user_data_path, "userkeys.key")

home_path = os.path.join(system_path, "home")

user_store = os.path.join(user_data_path, user_data)

password_store = os.path.join(user_data_path, password_data)

total_iterations = 100

def progress_bar(iteration, total, prefix='', suffix='', length=50, print_end='\r'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '#' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} [{bar}] {percent}% {suffix}',)
    sys.stdout.flush()
    if iteration == total:
        print(print_end)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

user = input("Please enter username for default user: ")
user_password = input("Please enter password for default user: ")

sleep(1.2)

print("Installing...")

os.mkdir(system_path)
os.mkdir(user_data_path)
os.mkdir(home_path)

with open(user_keys_path, "wb") as userkeys:
    userkeys.write(key)

f = open(user_store, "w")
f.write(user)
f.close()

f = open(password_store, "w")
f.write(user_password)
f.close()

for i in range(total_iterations + 1):
    sleep(0.04)
    progress_bar(i, total_iterations, prefix='Progress:', suffix='Complete', length=50)

print("SynOS has successfully installed")
sleep(0.8)
print("Rebooting...")
sleep(2)
clear_screen()
sleep(0.3)
os.system("python3 main.py")