import os
import sys
import time
from time import sleep
from cryptography.fernet import Fernet
from random import randint

system_path = "SynOS"

user_data = "username.txt"

password_data = "password.txt"

user_data_path = os.path.join(system_path, "users_data")

user_keys_path = os.path.join(user_data_path, "userkeys.key")

home_path = os.path.join(system_path, "home")

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

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

print("░██████╗██╗░░░██╗███╗░░██╗░█████╗░░██████╗\n██╔════╝╚██╗░██╔╝████╗░██║██╔══██╗██╔════╝\n╚█████╗░░╚████╔╝░██╔██╗██║██║░░██║╚█████╗░\n░╚═══██╗░░╚██╔╝░░██║╚████║██║░░██║░╚═══██╗\n██████╔╝░░░██║░░░██║░╚███║╚█████╔╝██████╔╝\n╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝░╚════╝░╚═════╝░")
print("Welcome to the SynOS Console. Please log in:")

sleep(1)

username = open(user_store, "r")
u_n = username.read()

password = open(password_store, "r")
u_p = password.read()

enterPassword = input("Password for " + u_n + ": ")

if enterPassword == u_p:
    print("Welcome back, " + u_n)
else:
    print("Error: Incorrect password")

#print(os.getcwd())

while True:
    command = input(home_path + ":/>")
    
    if command == "exit":
        sys.exit()
    elif command == "clear":
        clear_screen()
    elif command == "ver":
        print("░██████╗██╗░░░██╗███╗░░██╗░█████╗░░██████╗\n██╔════╝╚██╗░██╔╝████╗░██║██╔══██╗██╔════╝\n╚█████╗░░╚████╔╝░██╔██╗██║██║░░██║╚█████╗░\n░╚═══██╗░░╚██╔╝░░██║╚████║██║░░██║░╚═══██╗\n██████╔╝░░░██║░░░██║░╚███║╚█████╔╝██████╔╝\n╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝░╚════╝░╚═════╝░")
        print("SynOS Console Beta 0.8. Created by Adam1000")
    