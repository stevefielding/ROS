#! /usr/bin/env python

import rospy
from exercise_22.msg import Age

rospy.init_node('age_publisher')
pub = rospy.Publisher('/age_info', Age, queue_size=1)
robAge = Age()
robAge.years = 1
robAge.months = 2
robAge.days = 3



rate = rospy.Rate(2)

while not rospy.is_shutdown(): 
  pub.publish(robAge)
  rate.sleep()