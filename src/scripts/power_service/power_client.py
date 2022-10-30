import rospy

class power_client:
    def __init__(self):
        pass

if __name__ == '__main__':
    rospy.init_node('power_client', anonymous = True)
    client = power_client()