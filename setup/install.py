import os
import sys
import time
import requests
from time import sleep
#from cryptography.fernet import Fernet
from random import randint

system_path = "SynOS"

user_data = "username.txt"

password_data = "password.txt"

#key = Fernet.generate_key()

user_data_path = os.path.join(system_path, "users_data")

#user_keys_path = os.path.join(user_data_path, "userkeys.key")

home_path = os.path.join(system_path, "home")

apps_path = os.path.join(home_path, "applications")

user_store = os.path.join(user_data_path, user_data)

password_store = os.path.join(user_data_path, password_data)

total_iterations = 100

def progress_bar(iteration, total, prefix="", suffix="", length=50, print_end="\r"):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = "#" * filled_length + "-" * (length - filled_length)
    sys.stdout.write(f"\r{prefix} [{bar}] {percent}% {suffix}",)
    sys.stdout.flush()
    if iteration == total:
        print(print_end)

def download_file_from_pastebin(pastebin_url, save_directory):
    try:
        response = requests.get(pastebin_url)
        if response.status_code == 200:
            file_name = pastebin_url.split('/')[-1]
            file_path = os.path.join(save_directory, file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded successfully to {file_path}")
        else:
            print("Failed to download the file. Invalid URL or server error.")
    except Exception as e:
        print(f"An error occurred: {e}")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

user = input("Please enter username for default user: ")
user_password = input("Please enter password for default user: ")

sleep(1.2)

print("Installing...")

if os.path.exists(system_path):
    os.system("rm -r SynOS")

os.mkdir(system_path)
os.mkdir(user_data_path)
os.mkdir(home_path)
os.mkdir(apps_path)

"""with open(user_keys_path, "wb") as userkeys:
    userkeys.write(key)"""

f = open(user_store, "w")
f.write(user)
f.close()

f = open(password_store, "w")
f.write(user_password)
f.close()

for i in range(total_iterations + 1):
    sleep(0.04)
    progress_bar(i, total_iterations, prefix="Progress", suffix="Complete", length=50)

print("SynOS has successfully installed")
sleep(0.8)
print("Rebooting...")
sleep(2)
clear_screen()
sleep(0.3)
os.system("python3 main.py")