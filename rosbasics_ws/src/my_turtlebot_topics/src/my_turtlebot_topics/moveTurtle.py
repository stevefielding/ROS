#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class MoveTurtle(object):
  def __init__(self):
    self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

  def pubOnce(self,cmd):
    num_connections = self.pub.get_num_connections()
    while num_connections == 0:
      num_connections = self.pub.get_num_connections()
    self.pub.publish(cmd)
    
  def move(self, linear, angular):
    twist = Twist()
    twist.linear.x = linear
    twist.angular.z = angular
    self.pubOnce(twist)
    
if __name__ == "__main__":
  rospy.init_node("MoveTurtleTest")
  moveTurtle = MoveTurtle()
  moveTurtle.move(0.5, 0.1)
  rospy.sleep(2)
  moveTurtle.move(0.0, 0.0)
