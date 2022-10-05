#!/usr/bin/env python

import rospy
import sys
from hello_world.srv import coordinates_check
from hello_world.srv import coordinates_checkRequest
from hello_world.srv import coordinates_checkResponse

def coordinates_check_client(x,y):
    rospy.wait_for_service('coordinates_service')
    try:
        coordinates_check_ = rospy.ServiceProxy('coordinates_service', coordinates_check)
        response = coordinates_check_(x, y)
        return response.result
    except rospy.ServiceException():
        print("Connection failed")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("%s [x y]"%sys.argv[0])
        sys.exit(1)
    s = coordinates_check_client(x, y)
    print(s)