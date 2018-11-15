#! /usr/bin/env python

import rospy

from std_srvs.srv import Trigger, TriggerResponse, TriggerRequest
from crashReader import CrashReader

class CrashDetectionService(object):
  
  def __init__(self, crashThres=10):
    print("Starting a CrashDetectionService")
    # create a crash reader with detect threshold of 10
    self.crashReader = CrashReader(crashThres)
    self.crashDetServer = rospy.Service('/sphero_crash_detect_server', Trigger, self.callback)

  def callback(self, request):
    #rospy.loginfo("callback called")
    crashDir = self.crashReader.read()
    response = TriggerResponse()
    if crashDir == "none":
      response.success = True
    else:
      response.success = False
    response.message = crashDir
    #rospy.loginfo("callback completed")
    return response
    
if __name__ == "__main__":
  rospy.init_node("crashDetectServiceServer")
  myService = CrashDetectionService(crashThres=5)
  rospy.spin()
