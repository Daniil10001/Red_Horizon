#! /usr/bin/env python

import rospy
from visualization_msgs.msg import MarkerArray,Marker

rospy.init_node('rviz_markers')

marker_pub = rospy.Publisher("/visualization_markers", MarkerArray, queue_size = 2)

markerArray = MarkerArray()

for i in range(2):
    marker = Marker()

    marker.header.frame_id = "map"
    marker.header.stamp = rospy.Time.now()

    # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
    marker.type = 1
    marker.id = i

    # Set the scale of the marker
    marker.scale.x = 1.0
    marker.scale.y = 0.1
    marker.scale.z = 1.0

    # Set the color
    marker.color.r = 0.0
    marker.color.g = 1.0*((i+1)%2)
    marker.color.b = 1.0*(i%2)
    marker.color.a = 1.0

    # Set the pose of the marker
    marker.pose.position.x = 2
    marker.pose.position.y = 1*i
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0

    markerArray.markers.append(marker)

while not rospy.is_shutdown():
  marker_pub.publish(markerArray)
  rospy.rostime.wallsleep(0.1)