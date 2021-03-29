from dhooks import Webhook, Embed
import os
import time
import random, string

os.system('cls')

print('''
(1) WebHook Spammer

(2) Multiple WebHook Spammer

''')

option = input("Option: ")

if option == "1":
    os.system('cls')
    print('''
    
    ''')
    weblink = input("(Enter WebHook): ")

    hook = Webhook(weblink)
    print('''
    
    ''')
    speed = float(input("(In Seconds) How Fast?: "))
    print('''
    
    ''')
    text = input("Text To Be Spammed: ")
    
    os.system('cls')




    while True:
        os.system('cls')
        print("Spamming.")
        time.sleep(speed)
        os.system('cls')
        print("Spamming..")
        hook.send(text)
        print("Spamming...")

##TMMR MAKE MULTIPLE WEBHOOK SPAM

##AND A TITLE

if option == "2":
    os.system('cls')
    print('''
    
    ''')
    weblink1 = input("(Enter WebHook): ")
    os.system('cls')
    weblink2 = input("(Enter WebHook): ")
    os.system('cls')

    text = input("Text To Be Spammed: ")
    speed = float(input("(In Seconds) How Fast?: "))
    os.system('cls')

    hook1 = Webhook(weblink1)
    hook2 = Webhook(weblink2)

    while True:
        hook1.send(text)
        hook2.send(text)
        time.sleep(speed)