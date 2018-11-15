#! /usr/bin/env python
import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

# We create some constants with the corresponing vaules from the SimpleGoalState class
PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

"""
These appear to be ethe correct constants
  uint8 PENDING=0
  uint8 ACTIVE=1
  uint8 PREEMPTED=2
  uint8 SUCCEEDED=3
  uint8 ABORTED=4
  uint8 REJECTED=5
  uint8 PREEMPTING=6
  uint8 RECALLING=7
  uint8 RECALLED=8
  uint8 LOST=9
"""

nImage = 1

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

# I have no idea why the takeoff command must be issued multiple times with a delay
def pubNTimesWithDelay(pub, n, delay):
  rateLocal = rospy.Rate(delay)
  empty = Empty()
  i=0
  while i < n:
    pub.publish(empty)
    rateLocal.sleep()
    i += 1
 
# initializes the action client node
rospy.init_node('drone_action_client')

# get the drone to takeoff
print("Taking off")
pubTakeOff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
pubNTimesWithDelay(pubTakeOff, 3, 1)

# create the connection to the action server
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)
# waits until the action server is up and running
client.wait_for_server()

# creates a goal to send to the action server
goal = ArdroneGoal()
goal.nseconds = 10 # indicates, take pictures along 10 seconds

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)

# Uncomment these lines to test goal preemption:
#time.sleep(3.0)
#client.cancel_goal()  # would cancel the goal 3 seconds after starting

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time 
status = client.get_state()
pubCmdVel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
twist = Twist()
rate = rospy.Rate(1)

twist.linear.x = 0.0
twist.angular.z = 0.0
while status < DONE:
  print("Doing something whilst waiting")
  twist.angular.z += 0.05
  twist.linear.x += 0.05
  pubCmdVel.publish(twist)
  rate.sleep()
  status = client.get_state()
  
if status == DONE:
  print("[INFO] finished moves successfully")
elif status == ERROR:
  print("[ERROR] During moves")
elif status == WARN:
  print("[WARNING] During moves")
  
# check the client API link below for more info

#client.wait_for_result()

# get the drone to land
print("Landing")
twist.angular.z = 0.0
twist.linear.x = 0.0
pubCmdVel.publish(twist)
rate.sleep()
pubLand = rospy.Publisher('/drone/land', Empty, queue_size=1)
pubNTimesWithDelay(pubLand, 3, 1)

print('[Result] State: %d'%(client.get_state()))
