import rospy
from hello_world.srv import coordinates_check
from hello_world.srv import coordinates_checkRequest
from hello_world.srv import coordinates_checkResponse

#funkcja tworzaca odp 
def handle_coordinates_check(req):
    #jesli dystans od punktu odniesienia jest wiekszy niz 100(nominalny zasieg) odeslij false 
    if(req.x**2 + req.y**2 < 10000):
        response = coordinates_checkResponse(True)
    else:
        response = coordinates_checkResponse(False)
    return response    

#funkcja odpowiadajaca za sam serwer

def coordinates_check_server():
    rospy.init_node('coordinates_chceck_server', anonymous = True)
    s = rospy.Service('coordinates_service', coordinates_check, handle_coordinates_check)
    #Service z duze litery pamietaj XDDD
    print("Ready to get request: ")
    rospy.spin()

if __name__ == '__main__':
    #wywolanie funkcji odpowiedzialnej za serwer
    coordinates_check_server()