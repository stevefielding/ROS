#! /usr/bin/env python

import rospy

rospy.init_node('ObiWan')
rate = rospy.Rate(2)
while not rospy.is_shutdown():
  print "Help me Obi-Wan Kenobi, you're my only hope"
  rate.sleep()
  
# This program creates an endless loop that repeats itself 2 times per second (2Hz) until somebody presses Ctrl + C
# in the Shell
