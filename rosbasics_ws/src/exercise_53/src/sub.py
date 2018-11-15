#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty

rospy.init_node('sub_node')
rospy.Subscriber('/test1', Empty)

rate = rospy.Rate(1)
while not rospy.is_shutdown():
  rate.sleep()