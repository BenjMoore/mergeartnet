## Universe Merge Script (Contact Ben Moore [contact@theoasis.tech] for issues)
## TEST CASES ###
## TEST WITH NDI RUNNING ##
import datetime
import time
import os
import platform
from stupidArtnet import StupidArtnetServer
from stupidArtnet import StupidArtnet
import random
import sacn
import pyenttec as dmx
import blacklist

print("Init sACN")


global port
global blacklist_DB
port = ""
global dmxData
dmxData = []
global version
global grabOS # get_os does not work so manually speccing
grabOS = platform.system()
version = 1.0
author = "Ben Moore"
Soutput = ''

def main():
    get_os()
    splash()
    # blacklist.blacklist(blacklist)


def globalvar():
    version = 1.0
    return version

def initiatesACN():   
    # Define & initiate sACN (E1.31) receiver
    receiver = sacn.sACNreceiver()
    receiver.start()  # start the receiving thread

def currentRunning():
    up = "Online"
    return up
    pass

global serialbusHardcode
serialbusHardcode = "usb-ENTTEC_DMX_USB_PRO_EN263321-if00-port0"

def getbus(serial_bus):
    # Soutput = input("Serial Bus to use (Set to NONE to not use Serial): ")
    # serial_bus = Soutput
    # if serial_bus == "":
    #    Soutput = serial_bus
    serial_bus = "usb-ENTTEC_DMX_USB_PRO_EN263321-if00-port0"
    print(serial_bus)

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

def blacklistStatus():
        if blacklist == []:
            # print("\u001b[32mBlacklist \u001b[31mEMPTY \033[0m\u001b[32m ==\033[0m", blacklist)
            # input("\u001b[32mPress \u001b[31mENTER\033[0m \u001b[32mto continue...\033[0m")
            print("Blacklist Disabled")
            pass
        else:
            # print("\u001b[32mBlacklist: \033[0m", blacklist)
            # input("\u001b[32mPress \u001b[31mENTER\033[0m \u001b[32mto continue...\033[0m")
            print("Blacklist Disabled")
            pass

def info():
        os.system(get_os())
        print("\u001b[35m|| sMAN -- INFO ||\033[0m")
        print("\u001b[32m+\033[0m"*18)
        print("\u001b[32m+\033[0m \033[1;33mVersion:    \033[0m",version)
        # print("\u001b[32m+\033[0m \033[1;33mBlacklist:  \033[0m",blacklist)
        print("\u001b[32m+\033[0m \033[1;33mStatus:     \033[0m",up)
        print("\u001b[32m+\033[0m \033[1;33mAuthor:     \033[0m",author)
        print("\u001b[32m+\033[0m"*18)
        input("\u001b[32mPress ENTER to continue...\033[0m")
        splash()

def splash():
    
    
        
    serial_bus = "None"
    up = currentRunning()
    os_type = get_os()

    if os_type:
        os.system(os_type)

    print("""
    \033[1;35m
     
          $$\      $$\  $$$$$$\  $$\   $$\ 
          $$$\    $$$ |$$  __$$\ $$$\  $$ |
 $$$$$$$\ $$$$\  $$$$ |$$ /  $$ |$$$$\ $$ |
$$  _____|$$\$$\$$ $$ |$$$$$$$$ |$$ $$\$$ |
\$$$$$$\  $$ \$$$  $$ |$$  __$$ |$$ \$$$$ |
 \____$$\ $$ |\$  /$$ |$$ |  $$ |$$ |\$$$ |
$$$$$$$  |$$ | \_/ $$ |$$ |  $$ |$$ | \$$ |
\_______/ \__|     \__|\__|  \__|\__|  \__|
                                                                           
            Emerge Church

    \033[1;31m[1]\033[0m \033[1;32mStart\033[0m
    \033[1;31m[2]\033[0m \033[1;32mAdd Blacklist\033[0m
    \033[1;31m[3]\033[0m \033[1;32mRemove Blacklist\033[0m
    \033[1;31m[4]\033[0m \033[1;32mCheck Blacklist Status\033[0m
    \033[1;31m[5]\033[0m \033[1;32mDatastream\033[0m
    \033[1;31m[0]\033[0m \033[1;32mInfo\033[0m
    \033[1;31m[BUS]\033[0m \033[1;32mAssign Bus (Set to NONE to ignore Serial output)\033[0m
    """)
    if up == "Online":
        print("\u001b[32mStatus: "+ up +"\033[0m")
    else:
        print("\033[1;31mStatus: "+ up + "\033[0m")
    
    # Define the menu options
    print(blacklist.return_list())
    mainSelection = input("\033[0m\033[1;32mUniverseMerge\033[0m\033[0;37m@\033[0m""\033[1;32m\033[0m > ")
    
    if mainSelection == '1':
        main()
        
    if mainSelection == '2':
        pass
        
    if mainSelection == '3':
        # blacklistEnable = disable_blacklist(blacklist)
        print("Blacklist:") #, blacklistEnable
        time.sleep(1)
        splash()

    if mainSelection == '4':
        blacklistStatus()
        
    if mainSelection == '5':
        pass

    if mainSelection == 'BUS':
        getbus(serial_bus)
       
    if mainSelection == '0':
        info()


    

    print("Init Serial")

    #This is a whole thing, it's going to be pain, the people are going to love it, revolutionary you could say

def OsCompat():
    if grabOS == "Darwin":
        print("\u001bMacs get a free pass from the woes of Serial, as autodetection is supported[0m") # Rare Mac W
        port == dmx.select_port() # Set port to use
    elif grabOS == "Linux":
        if serialbusHardcode == "":
            print("\u001b[35;1mYou need to set your Serial bus in settings.\n | You can find it by running \nls /dev/serial/by-id/. Set the setting to whatever it prints, e.g: usb-ENTTEC_DMX_USB_PRO_EN263321-if00-port0\u001b[0m")
        else:
            # port == dmx.select_port("/dev/" + serial_bus, auto=False)
            print("Break!")
            print('/dev/serial/by-id/' + serialbusHardcode)
            port == dmx.DMXConnection('/dev/serial/by-id/usb-ENTTEC_DMX_USB_PRO_EN263321-if00-port0')
    elif grabOS == "Windows":
        if serialbusHardcode == "":
            print("\u001b[35;1mYou need to set your Serial bus in settings.\n | You can find it by going to Device manager, and looking for 'Ports (COM & LPT)'. Set the setting to whatever it shows in brackets, \u001b[33;1me.g: COM3\u001b[0m")
        else:
            # port == dmx.select_port(serial_bus, auto=False)
            port == dmx.DMXConnection(serialbusHardcode)
    elif serialbusHardcode == "NONE": 
    #print(port.lower())
        pass
    else:
        print("Unknown Error! (Serial)")
        exit()

print("Init Blacklist")

def disable_blacklist(blacklist):
    blacklist = []
    return blacklist

print("Init Sends")

def sendSerial():
    port.dmx_frame[packet] # Ben will add array soon
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

    global packet
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

    # TO SEND PERSISTANT SIGNAL YOU CAN START THE THREAD
    a.start()							# start continuos sending
    #switch = input("Type 'STOP' to end session >> ")

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
        
print("Init Receiving")

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

def reciveVISTA():
    #############
    #Recive VISTA through sACN
    # provide an IP-Address to bind to if you want to send multicast packets from a specific interface
    # define a callback function

    # provide an IP-Address to bind to if you are using Windows and want to use multicast
    receiver = sacn.sACNreceiver()
    receiver.start()  # start the receiving thread

    # define a callback function
    @receiver.listen_on('universe', universe=int(1))  # listens on universe 1
    def callback(packet):  # packet type: sacn.DataPacket
    
        vista_data = packet.dmxData[1:512]  
        print(vista_data, datetime.now())  # print the received DMX

        # optional: if multicast is desired, join with the universe number as parameter
        # receiver.join_multicast(1)

        time.sleep(10)  # receive for 10 seconds

        # optional: if multicast was previously joined
        # receiver.leave_multicast(1)

    receiver.stop()
           
            
# def return_blacklist(blacklist):
#     print(blacklist)
#     return blacklist


main()

## Spencer and Ben XOXO ##
