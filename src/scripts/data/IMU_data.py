#!/usr/bin/env python

import serial.tools.list_ports
import rospy
from geometry_msgs.msg import Vector3

class data_receive():
    def __init__(self):
        rospy.init_node('IMU_data_pub', anonymous = True)
        self.pub = rospy.Publisher('Imu_data_topic', Vector3, queue_size = 15)
        self.ports = serial.tools.list_ports.comports()
        self.serialInst = serial.Serial()
        self.stm_port = '/dev/ttyACM0'
        self.serialInst.baudrate = 115200
        self.serialInst.port = self.stm_port
        self.portList = []
        #self.show_ports()
        self.data = Vector3()
        #self.rate = rospy.Rate(33)
        self.serialInst.open()
        
        while not rospy.is_shutdown():
            try:
                self.receive_data()
                rospy.loginfo(self.data)
                #self.rate.sleep()
                
            except rospy.ROSInterruptException:
                pass
    
    def show_ports(self):
        for oneport in self.ports:
            self.portList.append(str(oneport))
            print(str(oneport))
    def receive_data(self):
        for i in range(3):
            if self.serialInst.in_waiting:
                self.line = str(self.serialInst.readline())
                if self.line[2] == "X":           
                    self.data.x = float(self.line[5:-5])
                    #print("x = {}".format(self.data.x))
                if self.line[2] == "Y":            
                    self.data.y = float(self.line[5:-5])
                    #print("y = {}".format(self.data.y))                 
                if self.line[2] == "Z":            
                    self.data.z = float(self.line[5:-5])
                    #print("z = {}".format(self.data.z))  
            
if __name__ == '__main__':
    data_receive()


#jak dac na zawsze dostep do protu