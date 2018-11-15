#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerRequest

rospy.init_node("crashDetClient")
rospy.wait_for_service('/sphero_crash_detect_server')
try:
  crashDetClient2 = rospy.ServiceProxy('/sphero_crash_detect_server', Trigger)
except rospy.ServiceException, e:
  print "Service call failed: %s"%e
  
req = TriggerRequest()

ctrl_c = False
def shutdownhook():
  # works better than the rospy.is_shut_down()
  global ctrl_c
  print "shutdown time!"
  ctrl_c = True

rospy.on_shutdown(shutdownhook)

rate = rospy.Rate(10)
while not ctrl_c:
  results = crashDetClient2(req)
  if results.success == False:
    rospy.loginfo("Crash direction: {}".format(results.message))
  rate.sleep()

