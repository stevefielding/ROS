#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from sensor_msgs.msg import LaserScan
from exercise_22.msg import Prox

def callback(msg): 
  midIndex = len(msg.ranges) / 2
  tenDegrees = (len(msg.ranges) * 10) / 180 
  fwdRange = msg.ranges[midIndex - tenDegrees : midIndex + tenDegrees]
  fwdRange = sum(fwdRange) / len(fwdRange)
  rightRange = sum(msg.ranges[0 : tenDegrees]) / tenDegrees
  leftRange = sum(msg.ranges[: len(msg.ranges) - tenDegrees: -1]) / tenDegrees
  prox.right = rightRange
  prox.forward = fwdRange
  prox.left = leftRange
  pub.publish(prox)

rospy.init_node('topic_subscriber')
prox = Prox()
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/laser_prox', Prox, queue_size=1)
rospy.spin()
