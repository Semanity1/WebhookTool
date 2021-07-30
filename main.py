import encodings.idna
from sys import exit
import time
import json
import sys
import requests
import colorama
import time
import os
from colorama import Fore

colorama.init(convert=True)

def webhookspammer():
    print(Fore.BLUE + "[+] Enter The Webhook Link: ")
    webhook = input()
    print("[+] Enter The Message: ")
    message = input()
    try:
        while True:
            try:
                time.sleep(0.3)
                data = requests.post(webhook, json={"content" : message})
                if data.status_code == 204:
                    print("[+] Sent [" + message +"]")
            except:
                print("Error I webhooken")
                time.sleep(5)
                main()
    except KeyboardInterrupt:
        print("Succesfully Spammed The Webhhok :D")
        time.sleep(2)
        main()

def webhookdeleter():
    print(f"[{Fore.RED}>{Fore.RESET}] Webhook link ")
    webhook = input("Here:")
    delhook = requests.delete(webhook)
    the = requests.get(webhook)
    if the.status_code == 404:
      print(f"[{Fore.GREEN}>{Fore.RESET}] Webhook Deleted")

def menu():
    os.system('cls')
    print("[1] Webhook Spammer")
    print("[2] Webhook Deleter")
    print("[3] Exit")
    def askChoice():
        option = int(input("Enter your option: "))
        if option == 1:
            webhookspammer()
        elif option == 2:
            webhookdeleter() 
        elif option == 3:
            print("Thanks for using SemanityTools")
            exit()
        else:
            print("Invalid option.")    
            askChoice()
    askChoice()


if __name__ == "__main__":
    menu()
