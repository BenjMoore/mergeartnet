## Universe Merge Script (Contact Ben Moore [contact@theoasis.tech] for issues)

import time
import os
import platform
import socket
import struct
import pyartnet

global blacklist
global IP1
global IP2
global DestIP
IP1 = "192.168.0.0"
IP2 = "192.168.0.1"
blacklist = []


def currentRunning():
    up = "Offline"
    return up
    pass

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
    up = currentRunning()
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
                                                               |___/
        Emerge Church

    \033[1;31m[1]\033[0m \033[1;32mStart\033[0m
    \033[1;31m[2]\033[0m \033[1;32mAdd Blacklist\033[0m
    \033[1;31m[3]\033[0m \033[1;32mRemove Blacklist\033[0m
    \033[1;31m[4]\033[0m \033[1;32mCheck Blacklist Status\033[0m
    \033[1;31m[5]\033[0m \033[1;32mDatastream\033[0m
    \033[1;31m[0]\033[0m \033[1;32mInfo\033[0m
    \033[1;31m[IP]\033[0m \033[1;32mAssign IP\033[0m
    """)
    print("\033[1;31mStatus: "+ up + "\033[0m")
    # Define the menu options

    mainSelection = input("\033[0m\033[1;32mUniverseMerge\033[0m\033[0;37m@\033[0m\033[1;32mroot\033[0m > ")

    if mainSelection == '1':
        main()
        
    if mainSelection == '2':
        blacklistChannels()

    if mainSelection == '3':

        blacklistEnable = disable_blacklist()
        print("Blacklist:", blacklistEnable)
        time.sleep(1)
        splash()

    if mainSelection == '4':
        if len(blacklist) == 0:
            print("Blacklist Empty!")
            time.sleep(1)
            splash()
        else:
            print("Blacklist: ", blacklist)
            time.sleep(3)
            splash()
        
    if mainSelection == '5':
        pass
    if mainSelection == '0':
        print("Universe 1 IP: ",IP1)
        print("Universe 2 IP: ", IP2)
        print("Destination IP: ", DestIP)
        print("Blacklist: ", blacklist)
        input("Press Enter To Continue....")
        splash()
        
    if mainSelection == 'IP':
        IP1 = input("Universe 1: ")
        IP2 = input("Universe 2: ")
        DestIP = input("Destination IP: ")
        splash()
       

    else:
        print("Invalid Input...")
        time.sleep(1)
        print("Restarting...")
        time.sleep(1)
        splash()

def blacklistChannels():
    import csv
    blackListInfo = input("Blacklist channels? [Y/N]: ")
    if blackListInfo == "Y" or "y":
        channelsToBlacklist()

    if blackListInfo == "N" or "n":
        splash()
        pass

def channelsToBlacklist():
    import csv
    filename = input('Enter the CSV file name: ')

    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        blacklist = [row for row in csvreader]

    return blacklist
    

def disable_blacklist():
    blacklist = []



def main():

    # Set up Art-Net parameters
    ip_addresses = [IP1, IP2]  # IP addresses of the Art-Net nodes
    port = 6454  # Art-Net port
    universe_size = 512  # Number of channels in a single Art-Net universe
    num_universes = 2  # Number of universes to merge
    blacklist_channels = []  # List of channels to exclude from the merged data

    # Set up Art-Net sender to send merged data
    destination_ip = DestIP
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Create a buffer to hold the merged universe data
    merged_data = bytearray(universe_size * num_universes)

    # Loop through the universes to merge
    for universe in range(num_universes):
        # Connect to the Art-Net node for this universe
        address = (ip_addresses[universe], port)
        receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        receiver_socket.bind(address)

        # Receive the universe data from the Art-Net node
        data = receiver_socket.recv(universe_size)

        # Merge the universe data into the merged_data buffer
        start_index = universe * universe_size
        for i in range(universe_size):
            if i not in blacklist_channels:
                merged_data[start_index + i] = data[i]

        # Close the connection to the Art-Net node
        receiver_socket.close()

    # Send the merged universe data via Art-Net
    packet_size = 18 + len(merged_data)
    packet_data = struct.pack('!8sBHHH', b'Art-Net\x00', 0x00, packet_size, 0x00, 0x50) + merged_data
    sender_socket.sendto(packet_data, (destination_ip, port))

    # Close the socket
    sender_socket.close()



if __name__ == '__main__':
    splash()



## Spencer and Ben XOXO ##
