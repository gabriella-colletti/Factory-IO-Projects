from pymodbus.client.sync import ModbusTcpClient
import pymodbus.bit_read_message
import time
# Connecting the TCP Client to the Factory I/O Host
client = ModbusTcpClient('192.168.56.1', port = 502)
client.connect()
unit1 = 0x1
first_touch_sensor = False
passed_sensor_A = False
import time
while True:
    # Sensors reads False when the box is imbetween the sensor
    # Sensors reads True when nothing is imbetween the sensor
    sensor_B = client.read_discrete_inputs(0,1,unit=unit1).bits[0]
    sensor_A = client.read_discrete_inputs(1,1,unit=unit1).bits[0]
       
    if sensor_B:  # If the box is not at sensor B
        if passed_sensor_A == False:                 # If the box has not passed the first sensor (sensor A)
            client.write_coil(0,True, unit=unit1)    # Turn on the first conveyors
            time.sleep(0.1)
        else:     # If the box has passed the first sensor (sensor A)
            client.write_coil(0,False, unit=unit1)   # Turn off the first conveyor  
        client.write_coil(1,True, unit=unit1) # Turn on the latter conveyors until the box reaches sensor B
        time.sleep(0.1)
   
    if sensor_A == False:               # If box started touching sensor A
        first_touch_sensor = True       # Change first_touch_sensor flag to True

    if sensor_A and first_touch_sensor: # If the box has passed sensor A
        passed_sensor_A = True          # Change passed_sensor_A flag to True
       
    if sensor_B == False:
        client.write_coil(0,False, unit=unit1) # Turn off the conveyors
        client.write_coil(1,False, unit=unit1) # Turn off the conveyors
        time.sleep(0.1)
        first_touch_sensor = False  # Reset Booleans for next sim
        passed_sensor_A = False     # Reset Booleans for next sim
