import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys


#uruchamianie kamery w rosie
#$rosrun usb_cam usb_cam_node _pixel_format:=mjpeg


#sworzyc obiekt typu CvBridge
bridge = CvBridge()

def image_callback(ros_image):
    global bridge 

    #konwersja z typu rosa na typ opencv
    try: 
        cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as e:
        print(e)
    #od teraz pracujemy z obrazem tak jak zawsze w opencv
    cv2.imshow("Image Window", cv_image)
    cv2.waitKey(3)


def main(argv):
    rospy.init_node('image_converter', anonymous = True)
    image_sub = rospy.Subscriber('/usb_cam/image_raw', Image, image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("THe proces has been shot down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)

    #..
    #
    #
    #..