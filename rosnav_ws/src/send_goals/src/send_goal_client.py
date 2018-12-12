#! /usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseResult, MoveBaseGoal

class MoveHusky(object):
  def __init__(self):
    self.client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
    self.client.wait_for_server()
    self.goal = MoveBaseGoal()
    
  def moveToDest(self, x, y):
    self.goal.target_pose.header.frame_id = "map"
    self.goal.target_pose.pose.position.x = x
    self.goal.target_pose.pose.position.y = y
    self.goal.target_pose.pose.orientation.z = 0.7071
    self.goal.target_pose.pose.orientation.w = 0.7071
    rate = rospy.Rate(0.5)
    self.client.send_goal(self.goal)
    result = self.client.get_result()
    while result == None:
      result = self.client.get_result()
      status = self.client.get_state()
      rospy.loginfo("Status: {}".format(status))
      rospy.loginfo("Result: {}".format(result))
      rate.sleep()

if __name__ == "__main__":
  rospy.init_node("move_base_client")
  moveHusky = MoveHusky()
  while rospy.is_shutdown() == False:
    moveHusky.moveToDest(-4.0, 0.0)
    moveHusky.moveToDest(-4.0, -2.0)
    moveHusky.moveToDest(0.0, 0.0)
