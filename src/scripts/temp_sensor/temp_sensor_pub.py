#!/usr/bin/env python
import rospy
from hello_world.msg import temp_sensor
import random



#Topic initialization
pub = rospy.Publisher('temp_sensor_topic', temp_sensor, queue_size = 10)

#Node initialization
rospy.init_node('temp_sensor_pub', anonymous=True)

#set frequency
rate = rospy.Rate(1)

i = 0
while not rospy.is_shutdown():   
    Temp_sensor = temp_sensor()
    Temp_sensor.id = 1
    Temp_sensor.time = i
    Temp_sensor.temperature = 20 +random.random()
    rospy.loginfo(Temp_sensor)
    pub.publish(Temp_sensor)
    rate.sleep()
    i = i+1
