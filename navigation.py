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
from geometry_msgs.msg import PoseStamped, Point, Quaternion,Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from visualization_msgs.msg import MarkerArray,Marker

cord=[(1,3)]
p=[]
rospy.init_node('telem')

marker_pub = rospy.Publisher("/visualization_markers", MarkerArray, queue_size = 2)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)

markerArray = MarkerArray()

tf_buffer = tf2_ros.Buffer()  # tf buffer length
tf_listener = tf2_ros.TransformListener(tf_buffer)
rospy.sleep(1)

def pose(tr="aruco_map"):
    #print(rospy.Time.now())
    transform = tf_buffer.lookup_transform(tr, 'body', rospy.Time(rospy.Time.now().to_sec()-0.05))
    #print(transform)
    q=quaternion_from_euler(0,0,0)
    pose_transformed = tf2_geometry_msgs.do_transform_pose(PoseStamped(pose=Pose(position=Point(0,0,0), orientation=Quaternion(*q))), transform)
    #print(0)
    q=pose_transformed.pose.orientation
    p=pose_transformed.pose.position
    return p.x,p.y,p.z,euler_from_quaternion([q.x,q.y,q.z,q.w])[-1]


def navigate_wait(x=0, y=0, z=0, yaw=float('nan'), speed=0.5, frame_id='aruco_map', auto_arm=False, tolerance=0.1,tfi=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        xt,yt,zt,fit = pose('navigate_target')
        if math.sqrt(xt ** 2 + yt ** 2 + zt ** 2)< tolerance and abs(yaw-fit)<tfi:
            break
        rospy.sleep(0.2)

def get_tel():
    y_mx=4.5
    x_mx=7.5
    y_mn=-0.5
    x_mn=-0.5
    for i in range(60):
        print(i,p)
        navigate_wait(0,0,2,np.pi*i/180)
        xt,yt,zt,fit=pose()
        l=2
        xd=xt+l*np.sin(fit)
        yd=yt+l*np.cos(fit)
        if (x_mn<xd<x_mx and y_mn<yd<y_mx):
           
            p.append((xd,yd))

def Mark_P(x1,y1,x2,y2,id,maxid):
    marker = Marker()
    marker.header.frame_id = "map"
    marker.header.stamp = rospy.Time.now()
    marker.type = 1
    marker.id = id
    #Задаем размеры стены
    marker.scale.x = abs(x1-x2)+0.1
    marker.scale.y = abs(y1-y2)+0.1
    marker.scale.z = 1.5
    #Задаем цвет стены
    marker.color.r = 1.0*(1-id/maxid)
    marker.color.g = 1.0*(id/maxid)
    marker.color.b = 1.0
    marker.color.a = 1.0
    #Задаем координаты центра стены
    marker.pose.position.x = (x1+x2)/2
    marker.pose.position.y = (y1+y2)/2
    marker.pose.position.z = 0
    #Задаем поворот стены
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    return marker

get_tel()

for i in range(len(p)):
    markerArray.markers.append(Mark_P(p[i][0],p[i][1],p[i][0],p[i][1],i,len(p)-1))


while not rospy.is_shutdown():
  #Публикум массив маркеров в топик
  marker_pub.publish(markerArray)
  rospy.rostime.wallsleep(0.1)