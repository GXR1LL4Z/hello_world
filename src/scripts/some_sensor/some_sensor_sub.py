import rospy
from geometry_msgs.msg import Vector3

class some_sensor_sub:
    def __init__(self):
        self.sub = rospy.Subscriber('some_senosr_topic', Vector3, self.callback)
        rospy.spin()

    def callback(self, message):
        rospy.loginfo(rospy.get_caller_id() + "i heard: %lf" + message.data)
        
if __name__ == '__main__':
    rospy.init_node('some_sensor_sub', anonymous = True)
    some_sensor_sub