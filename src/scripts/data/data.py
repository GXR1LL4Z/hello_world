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
        line = str(serialInst.readline())
        
        if line[2] == "X":            
            if serialInst.in_waiting:
                line = str(serialInst.readline())
                data_test.x = float(line[2:-5])
                
        if line[2] == "Y":            
            if serialInst.in_waiting:
                line = str(serialInst.readline())
                data_test.y = float(line[2:-5])
                
        if line[2] == "Z":            
            if serialInst.in_waiting:
                line = str(serialInst.readline())
                data_test.z = float(line[2:-5])
        print(data_test)

#jesli odmoa dostepu do portu:
#sudo chmod 666 /dev/ttyACM0  
#dziwne to rozwiazanie 
#sprawdzic jak działa bez delaya
#jak wysyłac zmienne float przez uart