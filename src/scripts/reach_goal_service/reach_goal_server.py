from hello_world.srv import reach_goal
from hello_world.srv import reach_goalRequest
from hello_world.srv import reach_goalResponse
import rospy



class reach_goal_server:
    def __init__(self):
        self.s = rospy.Service('reach_goal', reach_goal, self.handle_reach_goal)
        print("gotowy")
        rospy.spin()

    def handle_reach_goal(self, request):
        dx = request.x_goal - request.x
        dy = request.y_goal - request.y
        dz = request.z_goal - request.z
        # print(request.x_goal)
        # print(request.y_goal)
        # print(request.z_goal)
        # print(request.x)
        # print(request.y)
        # print(request.z)
        # print(dx)
        # print(dy)
        # print(dz)
        while True:
            dx = request.x_goal - request.x
            dy = request.y_goal - request.y
            dz = request.z_goal - request.z
            if dx == 0 and dy == 0 and dz ==0:
                return reach_goalResponse(True)
            else:
                #return reach_goalResponse(False)
                request.x = request.x + dx
                request.y = request.y + dy
                request.z = request.z + dz



if __name__ == '__main__':
    rospy.init_node('reach_goal_server', anonymous = True)
    reach_goal_server() 