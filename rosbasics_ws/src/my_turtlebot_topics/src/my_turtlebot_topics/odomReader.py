#! /usr/bin/env python

import rospy
#rostopic info /odom
#Type: nav_msgs/Odometry
from nav_msgs.msg import Odometry

class OdomReader(object):
  def __init__(self):
    self.sub = rospy.Subscriber('/odom', Odometry, self.callback)
    rospy.wait_for_message('/odom', Odometry)
    rospy.loginfo("LaserReader started")
    self.topicData = None
    
  def callback(self, msg):
    self.topicData = msg
    
  def read(self):
    # read odom position
    # y positive is down, y negative is up
    # x positive is left, x negative is left
    # Regular Cartesian co-ordinates
    pos_x = self.topicData.pose.pose.position.x
    pos_y = self.topicData.pose.pose.position.y
    
    # As tbot is rotated, x and y do not vary, but z varies
    # z is always 0 when tbot is pointing left, and is either +1 or -1 when tbot is pointing right
    # This looks like quaternians
    orient_z = self.topicData.pose.pose.orientation.z
    
    return pos_x, pos_y, orient_z

if __name__ == "__main__":
  rospy.init_node("OdomReaderTest")
  odomReader = OdomReader()
  rospy.sleep(1)
  print(odomReader.read())
