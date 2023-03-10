#### MERGEARTNET LOGIN ####
from getpass import getpass
import os, time
f = 0
## Simple login script to ensure authorised acsess ##
class globalvar:
    def version():
        global Ver
        Ver = 1.0
        return Ver

globalvar.version()
os.system('clear')
print("\u001b[31mMergeartnet \u001b[32mV",Ver,"\u001b[0m\n\u001b[31mProduction Enviroment, BE CAREFULL\u001b[0m")
global username
database = {"Ben": "Oasis2023$", "admin": "root"}
username = input("\u001b[32mEnter Your Username : \u001b[0m")
os.system('clear')
print("\u001b[35mWelcome! <\u001b[32m",username,"\u001b[0m\u001b[35m>. Please enter your password.\n\u001b[0m")
password = getpass("\u001b[32mEnter Your Password : \u001b[0m")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            while f != 3:
                os.system('clear')
                f = f + 1
                print("\u001b[31mIncorrect Attempts ",f,"/3\u001b[0m")
                password = getpass("\u001b[32mEnter Your Password Again : \u001b")
                if f == 3:
                    os.system('clear')
                    print("\u001b[31mLogin Failed, Too many attempts, Contact Administrator\u001b[0m")
                    time.sleep(5)
                    quit()
                break

        os.system('clear')
        print("\u001b[33mWelcome To SillyMergeArtNet!! Try not to break it...\u001b[0m")
        os.system("python merge.py")
       
