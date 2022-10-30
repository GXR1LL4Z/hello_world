import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose 
import math
import time


x = 0
y = 0
yaw = 0

def pose_callback(pose_message):
    global x
    global y 
    global yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def move(velocity_publisher, speed, distance, is_forward):

    #deklaracja zmiennej typu twist do wysyania msg na cmd_vel_topic
    velocity_message = Twist()

    #odbieranie aktualnej lokalizacji
    global x, y
    x0 = x          #zapis pozycji startowej 
    y0 = y          #zapis pozycji startowej

    #sprawzenie flagi is_forward
    if(is_forward):
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = -abs(speed)
    
    #zmienna do sprawdzania ile dystansu zostao pokonane
    distance_moved = 0

    #czestotliwosc publikowania wiadomosci
    loop_rate = rospy.Rate(10)

    #petla w ktorej odbywa sie ruch 
    while True:
        rospy.loginfo("Turtlesim moves :)")
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()
        distance_moved = math.sqrt((x - x0)**2 + ((y - y0)**2))
        print ("Distance moved = {}".format(distance_moved))
        if not (distance_moved < distance):
            print("Dotarlem do celu.")
            break

    #zatrzymanie
    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)

def rotate_motion(velocity_publisher, angular_speed_d, angle, is_clockwise):
    #deklaracja zmiennej typu twist do wysyania msg na cmd_vel_topic
    velocity_message = Twist()
    #wyzerowanie wszytskich wartosci velocity_message typu Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0
    #odbieranie aktualnej lokalizacji
    global yaw
    #zapis pozycji startowej
    yaw0 = yaw

    #przeliczenie stopni na radiany, ROS uzywa radianow!
    angular_speed = math.radians(abs(angular_speed_d))
    
    #sprawdzenie flagi is_clockwise
    if(is_clockwise):
        velocity_message.angular.z = -abs(angular_speed)
    else:
        velocity_message.angular.z = abs(angular_speed)
    
    #czestotiwosc publikowania
    loop_rate = rospy.Rate(50)
    
    #obrocony kat
    angle_moved = 0
    #czas t0, rozpoczecia petli
    t0 = rospy.Time.now().to_sec()

    while True:
        #opublikowanie predkosci katowe do zolwika
        rospy.loginfo("Turtle turns :)")
        velocity_publisher.publish(velocity_message)
        
        #pobranie aktualnego czasu
        t1 = rospy.Time.now().to_sec()

        #aktualny kat obrotu
        angle_moved = (t1-t0) * angular_speed_d
        print ("Angle moved = {}".format(angle_moved))
        print ("current yaw = {}".format(yaw))
        loop_rate.sleep()
        #sprawdzenie 
        if not (angle_moved < angle):
            velocity_message.angular.z = 0
            velocity_publisher.publish(velocity_message)
            print("Dotarlem do celu :)")
            break

def go_to_goal(velocity_publisher, x_goal, y_goal):

    #odczytanie obecnej pozycji
    global x
    global y

    #tworzenie zmiennej typu Twist()
    vellocity_message = Twist()

    #czestotliwosc publikowania
    loop_rate = rospy.Rate(10)

    #petla ruchu
    while True:
        #stała ruchu liniowego i stala ruchu obrotowego
        c_linear = 0.5
        c_angular = 4.0

        #obliczenie dystansu miedzy celem a aktualna pozycja 
        distance = abs(math.sqrt((x_goal - x)**2 + (y_goal - y)**2))

        #obliczenie kata miedzy obecna pozycja a celowym
        angle_goal = math.atan2(y_goal - y, x_goal - x)

        #nadanie predkosci liniowej i katowe w zaleznosci od dystansu
        linear_speed = c_linear * distance
        angular_speed = (angle_goal - yaw) * c_angular

        #przypisanie w odpowiednie miejsca zmiennej velocity_message typu Twist() wartosci policzonych wyzej
        vellocity_message.linear.x = linear_speed
        vellocity_message.angular.z = angular_speed

        velocity_publisher.publish(vellocity_message)
        print("X = {} Y = {} Yaw = {}".format(x, y, yaw))

        loop_rate.sleep()

        #sprawdzenie czy obiekt dotarl na miejsce
        if (distance < 0.1):
            break
        
def set_orientation(velocity_publisher, speed_degree, angle_degree):
    #odczyt aktualnej pozycji katowej
    global yaw

    #przeliczenie stopni na radiany
    angle_radians = math.radians(angle_degree) - yaw
    
    #flaga, w kt strone szybciej sie odwroci
    clockwise = 0

    if angle_radians < 0:
        clockwise = 1
    else:
        clockwise = 0
        
    rotate_motion(velocity_publisher, speed_degree, math.degrees(abs(angle_radians)), clockwise)
    print("Kat obrotu = {}".format(math.degrees(angle_radians)))
    print("Zadany kat = {}".format(angle_degree))

def spiral_clean(velocity_publisher, rk, wk):
    
    
    velocity_message = Twist()
    global x
    global y
    loop_rate = rospy.Rate(1)

    while x < 10.5 and y<10.5 :
        rk = rk+0.1
        velocity_message.linear.x = rk
        velocity_message.linear.y = 0
        velocity_message.linear.z = 0
        velocity_message.angular.x = 0
        velocity_message.angular.y = 0
        velocity_message.angular.z = wk
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

    velocity_message.linear.x = 0
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)


#WIEKSZA CZESTOTLIWOSC DA WIEKSZA DOKLADNOSC !!!

if __name__ == '__main__':
    try:
        #inicjalizacja node
        rospy.init_node('turtlesim_cleaner_node', anonymous = True)

        #inicjalizacja publisgeera
        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

        #inicjalizacja subscribera
        pose_topic = '/turtle1/pose'
        pose_subscriber = rospy.Subscriber(pose_topic, Pose, pose_callback)
        time.sleep(2)

        #parametry zdefiniowane w pliku cleaner_app.launch
        x_goal = rospy.get_param("x_goal")
        y_goal = rospy.get_param("y_goal")

        #wywolania funkcji sekwencji ruchow
        #move(velocity_publisher, 1, 4, False)
        #rotate_motion(velocity_publisher, 45, 270, True)
        #go_to_goal(velocity_publisher, 2, 2)
        #set_orientation(velocity_publisher, 30, 240)
        #spiral_clean(velocity_publisher, 0, 2)
        go_to_goal(velocity_publisher, x_goal, y_goal)
    except rospy.ROSInterruptException():
        rospy.loginfo("Node terminated.")


