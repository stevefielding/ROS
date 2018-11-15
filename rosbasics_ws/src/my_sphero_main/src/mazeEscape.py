#! /usr/bin/env python

''' 
    1. Calls a service that tells you if it has crashed and in what direction you 
    should move.
    2. Moves the sphero based on the service response.
    3. Checks if it has exited the maze or the time given has run out. If so, 
    the program ends.
    
    Assume that the service /sphero_crash_detect_server is running.
    Assume that the action service server /spheroDistActionServer is running.
    
    Create a /sphero_crash_detect_server client
    Create a /cmd_vel publisher via moveWriter helper class
    Create a /spheroDistActionServer action client
'''

import rospy
from std_srvs.srv import Trigger, TriggerRequest
from my_sphero_actions.msg import getOdomDataAction, getOdomDataResult, getOdomDataGoal
from move_writer import MoveSphero
import actionlib

def getNextDir(currDir, crashDir):
  if crashDir == "left":
    nextDir = "right"
  elif crashDir == "right":
    nextDir = "left"
  elif crashDir == "front":
    if  currDir == "back":
      nextDir = "fwd"
    else:
      nextDir = "back"
  elif crashDir == "back":
    if  currDir == "fwd":
      nextDir = "back"
    else:
      nextDir = "fwd"
  elif crashDir == "up" or crashDir == "down":
    if currDir == "fwd":
      nextDir = "back"
    elif currDir == "back":
      nextDir = "fwd"
  else:
    nextDir = "fwd"
  return nextDir
  
rospy.init_node("mazeEscape")
rospy.loginfo("Starting Maze escape")

# init crash det service client
rospy.loginfo("Init crash det client")
crashDetServiceName = '/sphero_crash_detect_server'
crashDetReq = TriggerRequest()
rospy.wait_for_service(crashDetServiceName)
crashClient = rospy.ServiceProxy(crashDetServiceName, Trigger)

# init Sphero dist action service client
rospy.loginfo("Init sphero dist client")
spheroDistActionServerName = '/spheroDistActionServer'
spheroDistActionClient = actionlib.SimpleActionClient(spheroDistActionServerName, getOdomDataAction)
spheroDistActionClient.wait_for_server()
goal = getOdomDataGoal()
spheroDistActionClient.send_goal(goal)

# init Sphero Cmdvel topic publisher via MoveSphero
rospy.loginfo("Init moveSphero")
moveSphero = MoveSphero(0.02, 0.1)

# init some vars before loop
rate = rospy.Rate(20)
currDir = "fwd"
crashCnt = 0

# loop forever, move sphero, check for crashes, and change direction
rospy.loginfo("mazeEscape. Starting main loop")
while not rospy.is_shutdown():
  crashClientResults = crashClient(crashDetReq)
  
  # if crash detected then change direction
  if crashClientResults.success == False:
    crashCnt += 1
    #rospy.loginfo("Crash detected")
    crashDir = crashClientResults.message
    #rospy.loginfo("Crash direction: {}".format(crashDir))
    nextDir = getNextDir(currDir, crashDir)
    # if proposed nextDir is left or right, then move in that direction for
    # for 1 second, but don't update currDir
    if nextDir == "left" or nextDir == "right":
      moveSphero.move(nextDir)
      rospy.sleep(1.5)
    # else if proposed nextDir is fwd or back, then assign as new currDir
    elif nextDir == "fwd" or nextDir == "back":
      # after every 5 crashes, make a turn. This is to prevent Sphero
      # from simply going and back and forward between two parallel walls
      if crashCnt % 5 == 0:
        moveSphero.move("left")
        rospy.sleep(1)        
      currDir = nextDir
  # No crash detected, therefor move was successful
  #else:
  #  rospy.loginfo("Move success")
    
  rospy.loginfo("Moving in direction: {}".format(currDir))
  moveSphero.move(currDir)
  
  #spheroDistActionClient.wait_for_result()
  status = spheroDistActionClient.get_state()
  result = spheroDistActionClient.get_result()
  print(status)
  if status > 1:
    if status == 3:
      rospy.loginfo("Sucess, exited the maze")
    else:
      rospy.loginfo("Failed to exit the maze. Status: {}".format(status))
    break
  rate.sleep()

