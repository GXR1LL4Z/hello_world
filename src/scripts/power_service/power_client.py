from ast import Pass
import rospy

from hello_world.srv import power_service
from hello_world.srv import power_serviceRequest

class power_client:
    def __init__(self):
        #stworzyc clienta
        rospy.wait_for_service('power_service')
        self.client = rospy.ServiceProxy('power_service', power_service)
        request = power_serviceRequest(number = 2, power = 3)
        try:
            #zwrocenie wyniku
            response = self.client(request)
            rospy.loginfo("RESPONSE: "+ str(response))
        except rospy.ServiceException():
            pass

if __name__ == '__main__':
    rospy.init_node('power_client', anonymous = True)
    client = power_client()