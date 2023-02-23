## Universe Merge Script (Contact Ben Moore [contact@theoasis.tech] for issues)

#import argparse
import time
import os
import platform
#import socket
#import serial
#from pyartnet import ArtNetNode
#import pyenttec


def get_os():

    operating_system = platform.system()
    if operating_system == 'Linux':
        used_os = 'clear'
    elif operating_system == 'Windows':
        used_os = 'cls'
    elif operating_system == 'Darwin':
        used_os = 'clear'
    else:
        print('OS not defined!')
        used_os = None
    return used_os

def splash():

    os_type = get_os()
    if os_type:
        os.system(os_type)

    print("""
    \033[1;35m
      _    _       _                           __  __
     | |  | |     (_)                         |  \/  |
     | |  | |_ __  ___   _____ _ __ ___  ___  | \  / | ___ _ __ __ _  ___
     | |  | | '_ \| \ \ / / _ \ '__/ __|/ _ \ | |\/| |/ _ \ '__/ _` |/ _ \\
     | |__| | | | | |\ V /  __/ |  \__ \  __/ | |  | |  __/ | | (_| |  __/
      \____/|_| |_|_| \_/ \___|_|  |___/\___| |_|  |_|\___|_|  \__, |\___|
                                                                __/ |
        Emerge Church                                          |___/

    \033[1;31m[1]\033[0m \033[1;32mAdd Blacklist\033[0m
    \033[1;31m[2]\033[0m \033[1;32mRemove Blacklist\033[0m
    \033[1;31m[3]\033[0m \033[1;32mCheck Blacklist Status\033[0m
    \033[1;31m[4]\033[0m \033[1;32mRestart\033[0m
    \033[1;31m[5]\033[0m \033[1;32mDatastream\033[0m
    \033[1;31m[0]\033[0m \033[1;32mInfo\033[0m
    """)
    # Define the menu options

    mainSelection = input("\033[0m\033[1;32mUniverseMerge\033[0m\033[0;37m@\033[0m\033[1;32mroot\033[0m > ")

    if mainSelection == '1':
        blacklistChannels()

    else:
        print("Invalid Input...")
        time.sleep(1)
        print("Restarting...")
        time.sleep(1)
        splash()


def channelsToBlacklist():
    filename = input('Enter the CSV file name: ')

    data = []

    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        data = [row for row in csvreader]

    return data
    pass


def blacklistChannels():

    import csv

    blackListInfo = input("Blacklist channels? [Y/N]: ")

    if blackListInfo == "Y" or "y":
        channelsToBlacklist()

    if blackListInfo == "N" or "n":
        splash()
        pass



def main():
    parser = argparse.ArgumentParser(description='Merge two Art-Net universes and output them to an ENTTEC DMX USB Pro')
    parser.add_argument('192.168.1.184', type=str, help='IP address of the first Art-Net universe')
    parser.add_argument('192.168.1.148', type=str, help='IP address of the second Art-Net universe')
    parser.add_argument('blacklist', nargs=data, type=int, help='List of channels to blacklist')
    parser.add_argument('0.0.0.0', type=str, help='IP address of the output Art-Net universe', default=None)
    parser.add_argument('1936', type=int, help='Port of the output Art-Net universe', default=0x1936)
    #parser.add_argument('--usb-pro', type=str, help='Serial port of the ENTTEC DMX USB Pro', default=None)
    #parser.add_argument('--baud-rate', type=int, help='Baud rate of the ENTTEC DMX USB Pro', default=57600)
    args = parser.parse_args()

    # Set up the Art-Net universes
    universe1 = ArtNet(args.ip1, universe=0)
    universe2 = ArtNet(args.ip2, universe=0)

    # Set up the output Art-Net universe
    if args.output_ip is not None:
        output_universe = ArtNet(args.output_ip, universe=0, bind_ip=args.output_ip)
    else:
        output_universe = None

    # Set up the ENTTEC DMX USB Pro
    '''if args.usb_pro is not None:
        dmx = DMXUSBPro(port=args.usb_pro, baudrate=args.baud_rate)
    else:
        dmx = None'''

    # Merge the universes
    merged_universe = merge_universes(universe1.get(), universe2.get(), args.blacklist)

    # Output the merged universe
    if output_universe is not None:
        output_universe.set(merged_universe)

    # Output the merged universe to the ENTTEC DMX USB Pro
    if dmx is not None:
        dmx.setChannelRange(1, merged_universe)

    # Wait for a bit to give the DMX controller time to process the data
    f = open("log.txt", "a")
    a = print("Universe 1: [", universe1,"] | Universe 2: [",universe2,"]")
    f.write(a + "\n")
    print ("\033[A                             \033[A")

    time.sleep(0.1)




def merge_universes(universe1, universe2, blacklist):
    merged_universe = list(universe1)
    for i, channel in enumerate(universe2):
        if i in blacklist:
            continue
        if channel is not None:
            merged_universe[i] = channel
    return merged_universe


if __name__ == '__main__':
    splash()



## Spencer and Ben XOXO
