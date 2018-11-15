#! /usr/bin/env python

import rospy
import actionlib
from my_turtlebot_actions.odomActionServer import OdomActionServer
from my_turtlebot_topics.laserReader import LaserReader
from my_turtlebot_topics.crashDetServiceServer import CrashDetServiceServer
from my_turtlebot_topics.moveTurtle import MoveTurtle
from std_srvs.srv import Trigger, TriggerRequest
from my_turtlebot_actions.msg import record_odomAction, record_odomActionGoal, record_odomActionResult

# Start odom action server
MAZE_EXIT_TIMEOUT = 120
MAZE_EXIT_THRES = 10
rospy.init_node("maze_escape")
rospy.loginfo("Starting action server (mazeEscape): odomActionServer")
OdomActionServer(MAZE_EXIT_TIMEOUT, MAZE_EXIT_THRES)

# start crash detect server
CRASHDET_THRES_AHEAD = 1.0
CRASHDET_THRES_SIDE = 0.4
crashDetServiceServer = CrashDetServiceServer(CRASHDET_THRES_AHEAD, CRASHDET_THRES_SIDE)

# init turtlebot Cmdvel topic publisher via MoveTurtle
rospy.loginfo("Init MoveTurtle")
moveTurtle = MoveTurtle()

# init crash det client
crashDet = rospy.ServiceProxy('/turtlebotCrashDet', Trigger)
triggerRequest = TriggerRequest
#rate = rospy.Rate(0.2)
#while not rospy.is_shutdown():
#  response = crashDet()
#  print("Success: {}, nextDir: {}".format(response.success, response.message))
#  rate.sleep()


# init maze exit det client, and set goal
exitClient = actionlib.SimpleActionClient('/turtleBotExit', record_odomAction)
rospy.loginfo("Waiting for \"/turtleBotExit\" action server to start")
exitClient.wait_for_server()
rospy.loginfo("\"/turtleBotExit\" action server started")
goal = record_odomActionGoal()
exitClient.send_goal(goal)

# init some vars before loop
rate = rospy.Rate(1)
crashCnt = 0

# loop forever, move turtlebot, check for crashes, and change direction
LINEAR_VEL = 0.4
ANG_VEL = 0.5
rospy.loginfo("mazeEscape. Starting main loop")
while not rospy.is_shutdown():
  crashDetResults = crashDet()
  
  # if crash detected then change direction
  if crashDetResults.success == False:
    crashCnt += 1
    rospy.loginfo("Crash detected")
    
  nextDir = crashDetResults.message
  #rospy.loginfo("Crash direction: {}".format(crashDir))
  if nextDir == "ahead_left":
    moveTurtle.move(LINEAR_VEL,ANG_VEL)
  elif nextDir == "ahead_right":
    moveTurtle.move(LINEAR_VEL,-ANG_VEL)
  elif nextDir == "left":
    moveTurtle.move(0.0,ANG_VEL)
  elif nextDir == "right":
    moveTurtle.move(0.0,-ANG_VEL)
  elif nextDir == "ahead":
    moveTurtle.move(LINEAR_VEL,0.0)
  else:
    moveTurtle.move(LINEAR_VEL,0.0)

    
  rospy.loginfo("Moving in direction: {}".format(nextDir))

  
  #exitClient.wait_for_result()
  status = exitClient.get_state()
  result = exitClient.get_result()
  print(status)
  if status > 1:
    if status == 3:
      rospy.loginfo("Sucess, exited the maze")
    else:
      rospy.loginfo("Failed to exit the maze. Status: {}".format(status))
    break
  rate.sleep()





  
  

    
    
