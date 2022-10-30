import time
import rospy
from hello_world.srv import Area
from hello_world.srv import AreaRequest
from hello_world.srv import AreaResponse


#funkcja odpowiedzialna za liczenie pola
def handle_area(req):
    time.sleep(5)
    area_response = AreaResponse(req.a * req.b)
    return area_response


#inicjalizacja serwera 
def area_server():
    s = rospy.Service('area_service', Area, handle_area)    #tworzenie samego service
    rospy.init_node('area_server', anonymous = True)
    print("Ready to calculate area :)")
    rospy.spin()


if __name__ == '__main__':
    area_server()
