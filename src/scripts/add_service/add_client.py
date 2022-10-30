import rospy
import sys
from hello_world.srv import AddTwoInts
from hello_world.srv import AddTwoIntsRequest
from hello_world.srv import AddTwoIntsResponse

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        response = add_two_ints(x, y)
        return response.sum 
    except rospy.ServiceException():
        print("Connection failed %s !")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("%s [x y]"%sys.argv[0])
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    s = add_two_ints_client(x, y)
    print("%s + %s = %s"%(x, y, s))

