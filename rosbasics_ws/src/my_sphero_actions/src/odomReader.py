#! /usr/bin/env python

import rospy
from topic_reader import TopicReader
from nav_msgs.msg import Odometry
#from move_writer import MoveSphero

class OdomReader(object):

  def __init__(self):
    print("Starting an OdomReader")
    self.odomReader = TopicReader("/odom", Odometry)
    rospy.wait_for_message("/odom", Odometry)
    print("OdomReader running")
    
  def read(self):
    odomData = self.odomReader.read()
    return odomData      
          
if __name__ == "__main__":          
  rospy.init_node("OdomReader")
  rate = rospy.Rate(0.5)
  #moveSphero = MoveSphero(0.1, 0.5)
  odomReader = OdomReader()
  #rospy.sleep(2)
  
  curDir = "fwd"
  while not rospy.is_shutdown():
    #moveSphero.move(curDir)
    odomData = odomReader.read()
    rospy.loginfo("odomData: {}".format(odomData.pose.pose.position))
    rate.sleep()


  