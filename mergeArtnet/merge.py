## Universe Merge Script (Contact Ben Moore [contact@theoasis.tech] for issues)
## TEST CASES ###
## TEST WITH NDI RUNNING ##
import time
import os
import platform
from stupidArtnet import StupidArtnetServer
from ArtnetUtils import shift_this, put_in_range
from stupidArtnet import StupidArtnet
import random
import sacn

global blacklist
blacklist = []
global port
port = ""
global dmxData
dmxData = []
global version

# Define & initiate sACN (E1.31) receiver
receiver = sacn.sACNreceiver()
receiver.start()  # start the receiving thread


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
    \033[1;31m[BUS]\033[0m \033[1;32mAssign Bus (Set to NONE to ignore Serial output)\033[0m
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
        print("Blacklist: ", data)
        time.sleep(1)
        splash()
        
    if mainSelection == '5':
        pass
    if mainSelection == '0':
        pass

    if mainSelection == 'BUS':
        serial_bus = input("Serial Bus to use (Set to NONE to not use Serial): ")
        if serial_bus == "":
            serial_bus == "ttyUSB0"
        if serial_bus == lower(serial_bus):
            if serialNone == lower(serial_bus):
                return

       
    else:
        print("Invalid Input...")
        time.sleep(1)
        print("Restarting...")
        time.sleep(1)
        splash()

    #This is a whole thing, it's going to be pain, the people are going to love it, revolutionary you could say
    if operating_system == "Darwin":
        print("\u001bMacs get a free pass from the woes of Serial, as autodetection is supported[0m") # Rare Mac W
        port == dmx.select_port() # Set port to use
    elif operating_system == "Linux":
        if serial_bus == "":
            print("\u001b[35;1mYou need to set your Serial bus in settings.\n | You can find it by running \ndmesg | grep tty. Set the setting to whatever it prints, e.g: ttyUSB0\u001b[0m")
        else:
            port == dmx.select_port("/dev/" + serial_bus)
    elif operating_system == "Windows":
        if serial_bus == "":
            print("\u001b[35;1mYou need to set your Serial bus in settings.\n | You can find it by going to Device manager, and looking for 'Ports (COM & LPT)'. Set the setting to whatever it shows in brackets, \u001b[33;1me.g: COM3\u001b[0m")
        else:
            port == dmx.select_port(serial_bus)
    elif serial_bus == "NONE": 
    #print(port.lower())
        pass
    
    else:
        print("Unknown Error! (Serial)")
        exit()

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

def sendSerial():
    port.dmx_frame[1,2,3] # Ben will add array soon
    port.render()


def sendArtNet():
    target_ip = '192.168.1.58'		# typically in 2.x or 10.x range
    universe = 0										# see docs
    packet_size = 512								# it is not necessary to send whole universe

  
    
    # TARGET_IP   = DEFAULT 127.0.0.1
    # UNIVERSE    = DEFAULT 0
    # PACKET_SIZE = DEFAULT 512
    # FRAME_RATE  = DEFAULT 30
    # ISBROADCAST = DEFAULT FALSE
    a = StupidArtnet(target_ip, universe, packet_size, 30, True, True)

    # MORE ADVANCED CAN BE SET WITH SETTERS IF NEEDED
    # NET         = DEFAULT 0
    # SUBNET      = DEFAULT 0

    # CHECK INIT
    print(a)

    packet = bytearray(packet_size)		# create packet for Artnet
    for i in range(packet_size):			# fill packet with sequential values
        packet[i] = (i % 256)

    a.set(packet)						# only on changes

    a.set_single_value(1, 255)			# set channel 1 to 255

    a.show()							# send data

    a.flash_all()						# send single packet with all channels at 255

    time.sleep(1)						# wait a bit, 1 sec

    a.blackout()						# send single packet with all channels at 0
    a.see_buffer()

    # ALL THE ABOVE EXAMPLES SEND A SINGLE DATAPACKET
    # STUPIDARTNET IS ALSO THREADABLE
    # TO SEND PERSISTANT SIGNAL YOU CAN START THE THREAD
    a.start()							# start continuos sendin
    #switch = input("Type 'STOP' to end session >> ")
    # AND MODIFY THE DATA AS YOU GO

    while True:
        for x in range(512):
            for i in range(packet_size):  	# Fill buffer with random stuff
                packet[i] = random.randint(0, 255)
            a.set(packet)
            time.sleep(.2)

    if switch == 'STOP':
        a.blackout()
        a.stop()
        del a
        
def reciveresolume():
    print("===================================")
    print("Namespace run")

    # Art-Net 4 definition specifies nets and subnets
    # Please see README and Art-Net user guide for details
    # Here we use the simplified default
    UNIVERSE_TO_LISTEN = 0

    # Initilize server, this starts a server in the Art-Net port
    a = StupidArtnetServer()

    # For every universe we would like to receive,
    # add a new listener with a optional callback
    # the return is an id for the listener
    u1_listener = a.register_listener(
        UNIVERSE_TO_LISTEN, callback_function='')

    # print object state
    print("Object State:")
    print(a)

    # giving it some time for the demo
    time.sleep(3)

    # use the listener address to get data without a callback
    buffer = a.get_buffer(u1_listener)
    print(buffer)
    # Cleanup when you are done
   
#############
#Recive VISTA through sACN
def reciveVISTA():
    # provide an IP-Address to bind to if you want to send multicast packets from a specific interface
    # define a callback function
    @receiver.listen_on('universe', universe=0)  # listens on universe 1
    def callback(packet):  # packet type: sacn.DataPacket
        pass
    a = callback(packet)
    print(packet.dmxData)  # print the received DMX data


        # optional: if multicast is desired, join with the universe number as parameter
    receiver.join_multicast(1)

    time.sleep(10)  # receive for 10 seconds

        # optional: if multicast was previously joined
    receiver.leave_multicast(1)

    receiver.stop()
            


#reciveresolume()


##send()

if __name__ == main():

    pass

## Spencer and Ben XOXO ##
