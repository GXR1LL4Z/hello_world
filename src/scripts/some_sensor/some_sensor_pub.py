import rospy
from geometry_msgs.msg import Vector3

class sensor_data_pub:

    def __init__(self):
        self.pub = rospy.Publisher('some_sensor_topic', Vector3, queue_size = 10)
        self.rate = rospy.Rate(1)
        try:
            self.publikowanie()
        except rospy.ROSInterruptException:
            pass

    def publikowanie(self):
        i = 0
        data = Vector3()
        while not rospy.is_shutdown():
            data.x = i
            data.y = i + 1
            data.z = i - 1
            rospy.loginfo(data)
            self.pub.publish(data)
            self.rate.sleep()
            i = i + 1

if __name__ == '__main__':
    rospy.init_node('some_sensor_pub', anonymous = True)
    sensor_data_pub()
        