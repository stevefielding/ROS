#! /usr/bin/env python

# cat Trigger.srv
# ---
# bool success   # indicate successful run of triggered service
# string message # informational, e.g. for error messages

import rospy
from std_srvs.srv import Trigger, TriggerResponse, TriggerRequest
from laserReader import LaserReader

class CrashDetServiceServer(object):
    
  def __init__(self, crashThres_ahead=0.7, crashThres_side=0.3):
    self.laserReader = LaserReader(crashThres_ahead, crashThres_side)
    self.crashDetService = rospy.Service('/turtlebotCrashDet', Trigger, self.callback)
    
  def callback(self, request):
    objectDir = self.laserReader.objectTooClose()
    response = TriggerResponse()
    response.success = False
    if objectDir == "right":
      nextDir = "ahead_left"
    elif objectDir == "ahead_right":
      nextDir = "left"
    elif objectDir == "left":
      nextDir = "ahead_right"
    elif objectDir == "ahead_left":
      nextDir = "right"
    else:
      nextDir = "ahead"
      response.success = True
    response.message = nextDir
    return response
    
if __name__ == "__main__":
  rospy.init_node("CrashDetServiceServer")
  crashDetServiceServer = CrashDetServiceServer()
  rospy.spin()
