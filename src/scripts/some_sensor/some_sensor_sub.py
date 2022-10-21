import rospy
from geometry_msgs.msg import Vector3

class some_sensor_sub:
    def __init__(self):
        self.sub = rospy.Subscriber('some_sensor_topic', Vector3, self.callback)
        rospy.spin()

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + " I heard: {}".format(data))
        
if __name__ == '__main__':
    rospy.init_node('some_sensor_sub', anonymous = True)
    some_sensor_sub()