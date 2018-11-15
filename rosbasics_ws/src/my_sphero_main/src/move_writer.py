#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class MoveSphero(object):

  def __init__(self, fwdSpeed, turnSpeed):
    #rospy.init_node('sphero_move_node')
    self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    #self.sub = rospy.Subscriber('/move_sphero', String, callback)
    self.twist = Twist()
    self.fwdSpeed = fwdSpeed
    self.turnSpeed = turnSpeed

  def move(self, direction):
    rospy.loginfo("Move: \"{}\"".format(direction))
    if direction == "right":
      self.twist.angular.z = self.turnSpeed
      self.twist.linear.x = 0.0
    elif direction == "left":
      self.twist.angular.z = - self.turnSpeed
      self.twist.linear.x = 0.0      
    elif direction == "fwd":
      self.twist.angular.z = 0.0
      self.twist.linear.x = self.fwdSpeed  
    elif direction == "back":
      self.twist.angular.z = 0.0
      self.twist.linear.x = - self.fwdSpeed  
    elif direction == "stop":
      self.twist.angular.z = 0.0
      self.twist.linear.x = 0.0  
    else:
      rospy.logwarn("Unrecognized direction: \"{}\"".format(direction))
      self.twist.angular.z = 0.0
      self.twist.linear.x = 0.0  
    self.pub.publish(self.twist)


if __name__ == '__main__':
  rospy.loginfo("Testing moveSphero")
  rospy.init_node('moveSphero')
  print('moveSphero')
  moveSphero = MoveSphero(0.02, 0.1)
  rospy.sleep(1)
  moveSphero.move("left")
  moveSphero.move("left")
  rospy.sleep(1)
  moveSphero.move("right")
  rospy.sleep(1)
  moveSphero.move("fwd")
  rospy.sleep(1)
  moveSphero.move("back")
  rospy.sleep(1)
  moveSphero.move("stop")
  rospy.sleep(1)
  #rospy.spin()