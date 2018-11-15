#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 
from exercise_22.msg import Prox

def callback(msg):
  rightRange = msg.right
  leftRange = msg.left
  forwardRange = msg.forward
  
  if rightRange < 1:
    twist.linear.x = 0.0
    twist.angular.z = 0.5
  elif leftRange < 1:
    twist.linear.x = 0.0
    twist.angular.z = -0.5
  elif forwardRange < 1:
    twist.linear.x = 0.0
    twist.angular.z = 0.5
  else:
    twist.linear.x = 0.5
    twist.angular.z = 0.0
  pub.publish(twist)
  
rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/laser_prox', Prox, callback)
twist = Twist()
rospy.spin()



