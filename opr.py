import numpy as np
import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import time
from sensor_msgs.msg import Range



bridge = CvBridge()

i=0
def find_dsk(data):
    cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')  # OpenCV image
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (6,7),  None)
    print(ret)
    # If found, add object points, image points (after refining them)
    if ret == True:
        cv2.imwrite(str(i)+'.jpg',cv_image)
        i+=1


image_sub = rospy.Subscriber('main_camera/image_raw_throttled', Image, find_dsk, queue_size=1)