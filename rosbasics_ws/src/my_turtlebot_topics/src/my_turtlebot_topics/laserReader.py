#! /usr/bin/env python

import rospy
import numpy as np

#rostopic info /kobuki/laser/scan
#Type: sensor_msgs/LaserScan
from sensor_msgs.msg import LaserScan

class LaserReader(object):
  def __init__(self, crashThres_ahead, crashThres_side):
    self.crashThres_ahead = crashThres_ahead
    self.crashThres_side = crashThres_side
    self.sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.callback)
    rospy.wait_for_message('/kobuki/laser/scan', LaserScan)
    rospy.loginfo("LaserReader started")
    self.topicData = None
    
  def callback(self, msg):
    self.topicData = msg
    
  def readRanges(self):
    myLen = len(self.topicData.ranges)
    #print("myLen: {}".format(myLen))
    rangeAhead = np.amin(self.topicData.ranges[int(myLen/2)-40 : int(myLen/2)+40])
    rangeLeft = np.amin(self.topicData.ranges[-1:-40:-1])
    rangeRight = np.amin(self.topicData.ranges[0:40])
    return rangeRight, rangeAhead, rangeLeft

  def objectTooClose(self):
    ranges = self.readRanges()
    rospy.loginfo("ranges: {}".format(ranges))
    crashDir = "none"
    if ranges[1] < self.crashThres_ahead:
      if ranges[0] < ranges[2]:
        crashDir = "ahead_right"
      else:
        crashDir = "ahead_left"
    elif ranges[0] < self.crashThres_side:
      crashDir = "right"
    elif ranges[2] < self.crashThres_side:
      crashDir = "left"
    rospy.loginfo("crashDir: {}".format(crashDir))
    return crashDir
    
if __name__ == "__main__":
  rospy.init_node("LaserReaderTest")
  laserReader = LaserReader(0.3)
  rospy.sleep(1)
  while not rospy.is_shutdown():
    print(laserReader.readRanges())
    print(laserReader.objectTooClose())
    rospy.sleep(1)