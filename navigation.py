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
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import PoseStamped, Point, Quaternion

cord=[(1,3)]
rospy.init_node('telem')

tf_buffer = tf2_ros.Buffer()  # tf buffer length
tf_listener = tf2_ros.TransformListener(tf_buffer)

rospy.sleep(1)
print(rospy.Time.now())
transform = tf_buffer.lookup_transform('map', 'body', rospy.Time(rospy.Time.now().to_sec()-0.05))
print(transform)
pose_transformed = tf2_geometry_msgs.do_transform_pose(PoseStamped(point=Point(0,0,0), orientation=Quaternion(0,0,0,0)), transform)
print(pose_transformed)