#! /usr/bin/env python
import rospy

import actionlib
from actionlib.msg import TestFeedback, TestResult, TestAction
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import time

class MoveSquareClass(object):
    


  def __init__(self):
    # creates the action server
    self._as = actionlib.SimpleActionServer("move_square_as", TestAction, self.goal_callback, False)
    self._as.start()
    self.ctrl_c = False
    
    # create messages that are used to publish feedback/result
    self._feedback = TestFeedback()
    self._result   = TestResult()

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
        rospy.loginfo("Publish in cmd_vel...")
        break
      else:
        rospy.loginfo("No connection to topic. Waiting for connection")  
        rate.sleep()
            
  def moveFwd(self, pubCmdVel, x):
    twist = Twist()
    twist.linear.x = x
    self.publish_once(pubCmdVel, twist)

  def turn(self, pubCmdVel, z):
    twist = Twist()
    twist.angular.z = z
    self.publish_once(pubCmdVel, twist)


  def moveStraightThenTurn(self, pubCmdVel, fwdVel):
    self.moveFwd(pubCmdVel, fwdVel)
    rospy.sleep(4)
    self.moveFwd(pubCmdVel, 0.0)
    rospy.sleep(2)
    self.turn(pubCmdVel, 0.35)
    rospy.sleep(4)
    self.turn(pubCmdVel, 0.0)
    rospy.sleep(1)
    
  def move_square(self, pubCmdVel, fwdVel):
    self._feedback.feedback = 1
    self._as.publish_feedback(self._feedback)
    self.moveStraightThenTurn(pubCmdVel, fwdVel)
    self._feedback.feedback = 2
    self._as.publish_feedback(self._feedback)
    self.moveStraightThenTurn(pubCmdVel, fwdVel)
    self._feedback.feedback = 3
    self._as.publish_feedback(self._feedback)
    self.moveStraightThenTurn(pubCmdVel, fwdVel)
    self._feedback.feedback = 4
    self._as.publish_feedback(self._feedback)
    self.moveStraightThenTurn(pubCmdVel, fwdVel)

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
    # this is the function that computes the Fibonacci sequence
    # and returns the sequence to the node that called the action server
    
    # helper variables
    r = rospy.Rate(1)
    success = True
    
    # get the drone to takeoff
    rospy.loginfo("Taking off")
    pubTakeOff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
    self.pubNTimesWithDelay(pubTakeOff, 3, 1)

    # publish info to the console for the user
    rospy.loginfo('"move_square_as": Executing')
    
    pubCmdVel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    startTime = time.time()
    self.move_square(pubCmdVel, goal.goal)
    durationTime = time.time() - startTime
    rospy.loginfo ("Drone movement took {} s".format(durationTime))
    
    # get the drone to land
    rospy.loginfo("Landing")
    pubLand = rospy.Publisher('/drone/land', Empty, queue_size=1)
    self.pubNTimesWithDelay(pubLand, 3, 1)
    
    # at this point, either the goal has been achieved (success==true)
    # or the client preempted the goal (success==false)
    # If success, then we publish the final result
    # If not success, we do not publish anything in the result
    success = True
    self._result.result = durationTime
    if success:
      rospy.loginfo('Succeeded Moving Drone')
      self._as.set_succeeded(self._result)
      
      
if __name__ == '__main__':
  rospy.init_node('moveDroneInSquare')
  MoveSquareClass()
  rospy.spin()
  