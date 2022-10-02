#!/usr/bin/env python
import rospy
import time
from hello_world.srv import AddTwoInts
from hello_world.srv import AddTwoIntsRequest
from hello_world.srv import AddTwoIntsResponse

#server is similar to subscriber 
#zawsze wykonuje sie callback function kiedy przychodzi request from client

def handle_add_two_ints(req):
    print("Returning %s + %s = %s"%(req.a, req.b, (req.a + req.b)))
    time.sleep(5) #5 sec
    sum_response = AddTwoIntsResponse(req.a + req.b)
    return sum_response


#inicjalizacja, tworzenie samego serwera
def add_two_ints_server():
    rospy.init_node('add_two_ints_server', anonymous = True)
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    #                 nazwa service  typ serwisu  callback fun wywoywana zawsze gdy przyjdzie request
    print("Ready to add ints: ")
    rospy.spin()

if __name__ == '__main__':
    add_two_ints_server() 