#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
import math

#header:
#  seq: 29899
#  stamp:
#    secs: 996
#    nsecs: 710000000
#  frame_id: "odom_frame"
#child_frame_id: "base_link"
#pose:
#  pose:
#    position:
#      x: 3.49949118608e-06
#      y: -0.0123126093949
#      z: 0.0634727440811
#    orientation:
#      x: 0.0
#      y: 0.0
#      z: 0.0
#      w: 1.0
#  covariance: [1e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1000000000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1000000000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1000000000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001]
#twist:
#  twist:
#    linear:
#      x: -8.37627226973e-08
#      y: -2.61640061054e-05
#      z: 0.0
#    angular:
#      x: 0.0
#      y: 0.0
#      z: 2.79410007516e-08
#  covariance: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]


def check_if_out_maze(distTarget, odomList):
  startX, startY = odomList[0].pose.pose.position.x, odomList[0].pose.pose.position.y
  endX, endY = odomList[-1].pose.pose.position.x, odomList[-1].pose.pose.position.y
  dist = math.sqrt((endX - startX)**2 + (endY - startY)**2)
  rospy.loginfo("Distance from the origin: {}".format(dist))
  if dist >= distTarget:
    result = True
  else:
    result = False
  return result
  
    