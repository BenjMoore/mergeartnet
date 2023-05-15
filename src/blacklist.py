import os
import time

blacklist_DB = []

def blacklist(blacklist_DB):
    import csv
    blackListInfo = input("Blacklist channels? [Y/N]: ")
    if blackListInfo == "Y" or "y":
        import csv
        os.chdir('src/blacklists')
        filename = input('Enter the CSV file name: ')

        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            blacklist = [row for row in csvreader]
            print("Completed:")
            print("Current Blacklist: ",blacklist)
            time.sleep(1)
            return blacklist_DB
        
    if blackListInfo == "N" or "n":
        pass


def return_list():
    return blacklist_DB
    print(blacklist_DB)
    



