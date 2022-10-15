#!/usr/bin/env python
import serial.tools.list_ports
import rospy
from geometry_msgs.msg import Vector3


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

for oneport in ports:
    portList.append(str(oneport))
    print(str(oneport))

stm_port = '/dev/ttyACM0'
serialInst.baudrate = 115200
serialInst.port = stm_port
serialInst.open()
data_test = Vector3()
while True:
    if serialInst.in_waiting:
        line = serialInst.readline()
        line.decode('utf')
        
        if line.startswith(b"X"):
            data_test.x = line
            #print(data_test.x)
        if line.startswith(b"Y"):
            data_test.y = line
            #print(data_test.y)
        if line.startswith(b"Z"):
            data_test.z = line
            #print(data_test.z)
        print(data_test)

#jesli odmoa dostepu do portu:
#sudo chmod 666 /dev/ttyACM0  
