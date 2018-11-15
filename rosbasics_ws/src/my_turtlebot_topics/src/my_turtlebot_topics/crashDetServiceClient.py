#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerRequest, TriggerResponse


rospy.init_node("crashDetClientTest")
crashDet = rospy.ServiceProxy('/turtlebotCrashDet', Trigger)
triggerRequest = TriggerRequest
rate = rospy.Rate(0.2)
while not rospy.is_shutdown():
  response = crashDet()
  print("Success: {}, nextDir: {}".format(response.success, response.message))
  rate.sleep()
  