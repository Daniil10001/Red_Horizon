#! /usr/bin/env python

import rospy
from visualization_msgs.msg import MarkerArray,Marker

rospy.init_node('rviz_markers')

marker_pub = rospy.Publisher("/visualization_markers", MarkerArray, queue_size = 2)

markerArray = MarkerArray()

def Mark_Wall(x1,y1,x2,y2,id,maxid):
    marker = Marker()
    marker.header.frame_id = "map"
    marker.header.stamp = rospy.Time.now()
    marker.type = 1
    marker.id = id
    marker.scale.x = abs(x1-x2)+0.01
    marker.scale.y = abs(y1-y2)+0.01
    marker.scale.z = 1.5
    marker.color.r = 1.0*(1-id/maxid)
    marker.color.g = 1.0*(id/maxid)
    marker.color.b = 1.0
    marker.color.a = 1.0
    marker.pose.position.x = (x1+x2)/2
    marker.pose.position.y = (y1+y2)/2
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    return marker
cord=[(1,3),(3,3),(3,4),(4,4),(4,1),(5,1),(5,4),(6,4),(6,1),(7,1),(7,4)]
for i in range(len(cord)-1):
    markerArray.markers.append(Mark_Wall(cord[i][0],cord[i][1],cord[i+1][0],cord[i+1][1],i,len(cord)-1))

while not rospy.is_shutdown():
  marker_pub.publish(markerArray)
  rospy.rostime.wallsleep(0.1)