import rospy
from hello_world.srv import power_service
from hello_world.srv import power_serviceResponse

class power_server:
    def __init__(self):
        self.server = rospy.Service('power_service', power_service, self.handle_response)
        rospy.loginfo("SERVER HAS BEEN STARTED")

    def handle_response(self, request):
        rospy.loginfo("SERVER HAS RECEIVED REQUEST FROM CLIENT")
        response = power_serviceResponse()
        response.result = request.number**request.power
        return response

if __name__ == '__main__':
    rospy.init_node('power_server', anonymous = True)
    server = power_server()
    rospy.spin()