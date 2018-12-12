#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
from init_particles import Init_particles
import functools

class MoveWriter(object):

  def __init__(self):
    self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    self.pose_sub = rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, self.sub_callback)
    self.poseData = None
    init_particles = Init_particles()
    init_particles.init()
    
  def sub_callback(self, msg):
    #print("Got /amcl_pose topic data")
    self.poseData = msg
    
  def move(self, linear, angular, time):
    rate = rospy.Rate(10)
    for i in range(time):
      twist = Twist()
      twist.linear.x = linear
      twist.angular.z = angular
      self.pub.publish(twist)
      rate.sleep()

  def moveSquare(self, lenSide):
    self.move(1.5, 0.0, 20 * lenSide)
    self.move(0.0, 0.5, 45)
    self.move(1.5, 0.0, 20 * lenSide)
    self.move(0.0, 0.5, 45)
    self.move(1.5, 0.0, 20 * lenSide)
    self.move(0.0, 0.5, 45)
    self.move(1.5, 0.0, 20 * lenSide)
    self.move(0.0, 0.5, 45)
    self.move(0.0, 0.0, 2)

  def locationFound(self, thres):
    rate = rospy.Rate(5)
    rospy.loginfo("Waiting for pose data")
    while self.poseData == None:
      rate.sleep()
    covMat = self.poseData.pose.covariance
    varList = (covMat[0], covMat[7], covMat[14], covMat[21], covMat[28], covMat[35])
    rospy.loginfo("Pose covariance: {}".format(varList))
    # if all the variances are less than thres, then return True
    q = [i < thres for i in varList]
    varUnderThres = functools.reduce((lambda i,j: i==True and j==True), q)
    return varUnderThres
      
if __name__ == "__main__":
  rospy.init_node("square_move")
  moveWriter = MoveWriter()
  while moveWriter.locationFound(0.65) == False:
    moveWriter.moveSquare(1)
  
  