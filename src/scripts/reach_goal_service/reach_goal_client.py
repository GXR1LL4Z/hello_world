from hello_world.srv import reach_goal
from hello_world.srv import reach_goalRequest
from hello_world.srv import reach_goalResponse
import rospy
import sys

class reach_goal_client:    
    def __init__(self):
        self.request()

    def client(self, x_goal, y_goal, z_goal, x, y, z):
        rospy.wait_for_service('reach_goal')
        try: 
            reach_goals = rospy.ServiceProxy('reach_goal', reach_goal)
            response = reach_goals(x_goal, y_goal, z_goal, x, y, z)
            return response.result
        except rospy.ServiceException:
            pass

    def request(self):
        if len(sys.argv) == 7:
            x_goal = int(sys.argv[1])
            y_goal = int(sys.argv[2])
            z_goal = int(sys.argv[3])
            x = int(sys.argv[4])
            y = int(sys.argv[5])
            z = int(sys.argv[6])
            print(x_goal)
            print(y_goal)
            print(z_goal)
            print(x)
            print(y)
            print(z)
        else:
            sys.exit(1)
        result = self.client(x_goal, y_goal, z_goal, x, y, z)
        print("{}".format(result))

if __name__ == '__main__':
    reach_goal_client()