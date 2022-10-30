import rospy
from hello_world.msg import temp_sensor

def callback_temp_sensor(Temp_sensor):
    rospy.loginfo("New temp sensor data received: %d, %d, %f", Temp_sensor.id, Temp_sensor.time, Temp_sensor.temperature)

rospy.init_node('temp_sensor_sub_node', anonymous=True)
rospy.Subscriber('temp_sensor_topic', temp_sensor, callback_temp_sensor)
rospy.spin()


