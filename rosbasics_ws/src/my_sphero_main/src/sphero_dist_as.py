#! /usr/bin/env python

# This action server has to start recording the /odom topic and stop when a 
# certain time period has passed or the distance moved reaches a certain value.
# So the aim is to run for timeOut seconds, keep measuring the distance from the 
# origin. If this distance becomaes greater than distGoal, then quit, and return
# an array of all the /odom readings.
# goal
#---
# result
#nav_msgs/Odometry[] result_odom_array
#---
# feedback
#nav_msgs/Odometry[] feedback_odom_array

import rospy
import actionlib
from my_sphero_actions.msg import getOdomDataAction, getOdomDataFeedback, getOdomDataResult
from odomReader import OdomReader
from odometry_analysis import check_if_out_maze

class SpheroDistActionServer(object):

  def __init__(self, timeOut, distGoal):
    self.odomReader = OdomReader()
    self.getOdomDataActionServer = actionlib.SimpleActionServer("spheroDistActionServer", getOdomDataAction, self.goal_callback, False)
    self.getOdomDataActionServer.start()
    #self.feedback = getOdomDataFeedback()
    self.result = getOdomDataResult()
    self.odomData = []
    self.timeOut = timeOut
    self.distGoal = distGoal
    
  def goal_callback(self, msg):
    success = False
    rate = rospy.Rate(1)
    for curTime in range(self.timeOut):
      if self.getOdomDataActionServer.is_preempt_requested():
        rospy.logwarn("action server pre-empted")
        success = False
        break
      self.odomData.append(self.odomReader.read())
      #print(self.odomData)
      outOfMaze = check_if_out_maze(self.distGoal, self.odomData)
      if outOfMaze == True:
        success = True
        break
      rate.sleep()
    if success == True:
      self.result.result_odom_array = self.odomData
      self.getOdomDataActionServer.set_succeeded(self.result)
    else:
      rospy.loginfo("spehroDistActionServer timed out")
      
if __name__ == "__main__":
  rospy.init_node("spheroDistActionServer")
  rospy.loginfo("Starting action server: SpheroDistActionServer")
  SpheroDistActionServer(30,1)
  rospy.spin()
