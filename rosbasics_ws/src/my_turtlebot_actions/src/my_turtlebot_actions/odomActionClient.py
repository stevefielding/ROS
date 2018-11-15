#! /usr/bin/env python

import rospy
import actionlib
from my_turtlebot_actions.msg import record_odomAction, record_odomActionGoal, record_odomActionResult


'''
actionlib_msgs/msg/GoalStatus.msg
uint8 status
uint8 PENDING         = 0   # The goal has yet to be processed by the action server
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing
                            #   and has since completed its execution (Terminal State)
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due
                            #    to some failure (Terminal State)
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,
                            #    because the goal was unattainable or invalid (Terminal State)
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing
                            #    and has not yet completed execution
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,
                            #    but the action server has not yet confirmed that the goal is canceled
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing
                            #    and was successfully cancelled (Terminal State)
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be
                            #    sent over the wire by an action server
'''

rospy.init_node("turtlebotActionClient1")
client = actionlib.SimpleActionClient('/turtleBotExit', record_odomAction)
rospy.loginfo("Waiting for \"/turtleBotExit\" action server to start")
client.wait_for_server()
rospy.loginfo("\"/turtleBotExit\" action server started")
goal = record_odomActionGoal()
rate = rospy.Rate(0.2)

client.send_goal(goal)
rospy.sleep(1)
while not rospy.is_shutdown():
  result = client.get_result()
  status = client.get_state()
  rospy.loginfo("Status: {}".format(status))
  rospy.loginfo("Result: {}".format(result))
  rate.sleep()