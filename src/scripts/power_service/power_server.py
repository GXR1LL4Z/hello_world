import rospy

class power_server:
    def __init__(self):
        pass

if __name__ == '__main__':
    rospy.init_node('power_server', anonymous = True)
    server = power_server()
    rospy.spin()