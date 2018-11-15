#! /usr/bin/env python

import rospy
import actionlib
from my_turtlebot_actions.msg import record_odomAction, record_odomActionGoal, record_odomResult
from odomReader import OdomReader
import math

class OdomActionServer(object):

  def __init__(self, timeOut, distTarget):
    self.actionServer = actionlib.SimpleActionServer('turtleBotExit', record_odomAction, self.callback, False)
    self.actionServer.start()
    self.timeOut = timeOut
    self.distTarget = distTarget
    self.odomReader = OdomReader()
    self.result = record_odomResult()
    self.odomData = []
    rospy.loginfo("OdomActionServer instance created")

  def check_if_out_maze(self, distTarget, odomList):
    startX, startY = odomList[0][0:2]
    endX, endY = odomList[-1][0:2]
    dist = math.sqrt((endX - startX)**2 + (endY - startY)**2)
    #rospy.loginfo("Distance from the origin: {}".format(dist))
    if dist >= distTarget:
      result = True
    else:
      result = False
    return result
    
  def callback(self, goal):
    rospy.loginfo("odomActionServer goal requested")
    success = False
    rate = rospy.Rate(1)
    for curTime in range(self.timeOut):
      if self.actionServer.is_preempt_requested():
        rospy.logwarning("action server pre-empted")
        success = False
        break
      self.odomData.append(self.odomReader.read())
      #print(self.odomData)
      outOfMaze = self.check_if_out_maze(self.distTarget, self.odomData)
      if outOfMaze == True:
        success = True
        break
      rate.sleep()
    self.result.result_odom_array = self.odomData
    if success == True:
      self.actionServer.set_succeeded(self.result)
    else:
      rospy.loginfo("odomActionServer timed out")
      self.actionServer.set_aborted()

if __name__ == "__main__":
  rospy.init_node("odomActionServer")
  rospy.loginfo("Starting action server: odomActionServer")
  OdomActionServer(5,8)
  rospy.spin()