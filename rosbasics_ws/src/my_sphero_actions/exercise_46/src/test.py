#! /usr/bin/env python
import rospy
from std_msgs.msg import Empty

rospy.init_node('test')
pubTakeOff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)

empty = Empty()

rate = rospy.Rate(1)

i=0

while i < 4:
  pubTakeOff.publish(empty)
  rate.sleep()
  i += 1
  
#rospy.spin()
