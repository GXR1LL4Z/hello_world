#!/usr/bin/env python
import sys
import rospy
from hello_world.srv import Area
from hello_world.srv import AreaRequest
from hello_world.srv import AreaResponse

def area_client(x, y):
    rospy.wait_for_service('area_service')
    try:
        area = rospy.ServiceProxy('area_service', Area)
        response = area(x, y)
        return response.area
    except rospy.ServiceException():
        print("Connection failed due to!")

if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("%s [x y]"%sys.argv[0])
        sys.exit(1)
    print("Requesting %s*%s"%(x, y))
    s = area_client(x, y)
    print("%s * %s = %s"%(x, y, s))