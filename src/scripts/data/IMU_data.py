import serial.tools.list_ports
import rospy
from geometry_msgs.msg import Vector3
import re

class data_receive():
    def __init__(self):
        
        self.pub = rospy.Publisher('Imu_data_topic', Vector3, queue_size = 15)
        
        self.ports = serial.tools.list_ports.comports()
        self.serialInst = serial.Serial()
        self.stm_port = '/dev/ttyACM0'
        self.serialInst.baudrate = 115200
        self.serialInst.port = self.stm_port
        self.portList = []
        #self.show_ports()
        self.data = Vector3()        
        self.serialInst.open()
        
        
        while not rospy.is_shutdown():
            try:
                try:
                    self.receive_data()
                except ValueError:
                    #wyslij jeszcze raz poprzedni odczyt
                    pass
            except rospy.ROSInterruptException:
                pass
    
    def show_ports(self):
        for oneport in self.ports:
            self.portList.append(str(oneport))
            print(str(oneport))
            
    def receive_data(self):
        if self.serialInst.in_waiting:
            self.line = str(self.serialInst.readline())
            values = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", self.line)                
            if len(values) == 3:
                self.data.x = float(values[0])
                self.data.y = float(values[1])
                self.data.z = float(values[2])
            else:
                pass   
            rospy.loginfo(self.data)
            self.pub.publish(self.data)  

if __name__ == '__main__':
    rospy.init_node('IMU_data_pub', anonymous = True)
    data_receive()


#jak dac na zawsze dostep do protu