#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
twist = Twist()


while not rospy.is_shutdown(): 
  pub.publish(twist)
  if twist.linear.x == -1:
    twist.linear.x = 1
    twist.angular.x = 90
    twist.angular.y = 1
  else:
    twist.linear.x = -1
    twist.angular.x = 180
  rate.sleep()