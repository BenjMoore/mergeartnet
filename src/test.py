import sacn
import time

# provide an IP-Address to bind to if you want to send multicast packets from a specific interface
receiver = sacn.sACNreceiver()
receiver.start()  # start the receiving thread

# define a callback function
@receiver.listen_on('universe', universe=1)  # listens on universe 1
def callback(packet):  # packet type: sacn.DataPacket
    print(packet.dmxData)  # print the received DMX data

# optional: if multicast is desired, join with the universe number as parameter
receiver.join_multicast(1)

time.sleep(10)  # receive for 10 seconds

# optional: if multicast was previously joined
receiver.leave_multicast(1)

receiver.stop()