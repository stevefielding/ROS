#! /usr/bin/env python
import rospy

import actionlib
from exercise_413.msg import MoveUpdownFeedback, MoveUpdownResult, MoveUpdownAction
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import time

class MoveUpDownClass(object):
    


  def __init__(self):
    # creates the action server
    self._as = actionlib.SimpleActionServer("move_updown_as", MoveUpdownAction, self.goal_callback, False)
    self._as.start()
    self.ctrl_c = False
    
    # create messages that are used to publish feedback/result
    self._feedback = MoveUpdownFeedback()
    self._result   = MoveUpdownResult()

  def publish_once(self, pub, cmd):
    """
    This is because publishing in topics sometimes fails teh first time you publish.
    In continuos publishing systems there is no big deal but in systems that publish only
    once it IS very important.
    """
    while not self.ctrl_c:
      rate = rospy.Rate(1)
      connections = pub.get_num_connections()
      if connections > 0:
        pub.publish(cmd)
        break
      else:
        rospy.loginfo("No connection to topic. Waiting for connection")  
        rate.sleep()
            
  def moveUp(self, pubCmdVel, z):
    rospy.loginfo("Moving Up")
    twist = Twist()
    twist.linear.z = z
    self.publish_once(pubCmdVel, twist)
    self._feedback.currentdir = "UP"
    self._as.publish_feedback(self._feedback)
    rospy.sleep(1)
    twist.linear.z = 0.0
    self.publish_once(pubCmdVel, twist)
    
  def moveDown(self, pubCmdVel, z):
    rospy.loginfo("Moving Down")
    twist = Twist()
    twist.linear.z = -z
    self.publish_once(pubCmdVel, twist)
    self._feedback.currentdir = "DOWN"
    self._as.publish_feedback(self._feedback)
    rospy.sleep(1)
    twist.linear.z = 0.0
    self.publish_once(pubCmdVel, twist)
    
  # I have no idea why the takeoff command must be issued multiple times with a delay
  def pubNTimesWithDelay(self, pub, n, delay):
    rateLocal = rospy.Rate(delay)
    empty = Empty()
    i=0
    while i < n:
      pub.publish(empty)
      rateLocal.sleep()
      i += 1
    
  def goal_callback(self, goal):
    # this callback is called when the action server is called.

    # helper variables
    r = rospy.Rate(1)
    success = True
    
    # get the drone to takeoff
    #rospy.loginfo("Taking off")
    #pubTakeOff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
    #self.pubNTimesWithDelay(pubTakeOff, 3, 1)

    # publish info to the console for the user
    rospy.loginfo('"move_updown_as": Executing')
    
    pubCmdVel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    startTime = time.time()
    if goal.updown == "UP":
      self.moveUp(pubCmdVel, 1)
    elif goal.updown == "DOWN":
      self.moveDown(pubCmdVel, 1)
    else:
      rospy.loginfo("Unrecognized goal: \"{}\"".format(goal.updown))
      
    durationTime = time.time() - startTime
    rospy.loginfo ("Drone movement took {} s".format(durationTime))
    
    # get the drone to land
    #rospy.loginfo("Landing")
    #pubLand = rospy.Publisher('/drone/land', Empty, queue_size=1)
    #self.pubNTimesWithDelay(pubLand, 3, 1)
    
    self._as.set_succeeded()
    
if __name__ == '__main__':
  rospy.init_node('moveDroneUpDown')
  MoveUpDownClass()
  rospy.spin()
  