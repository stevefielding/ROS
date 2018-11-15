#! /usr/bin/env python

import rospy
from topic_reader import TopicReader
from sensor_msgs.msg import Imu
from move_writer import MoveSphero

class CrashReader(object):

  def __init__(self, thresh):
    print("Starting a CrashReader")
    self.imuReader = TopicReader("/sphero/imu/data3", Imu)
    rospy.wait_for_message("/sphero/imu/data3", Imu)
    print("CrashReader running")
    self.thres = thresh
    
  def read(self):
    imuData = self.imuReader.read()
    linAcc = imuData.linear_acceleration
    #rospy.loginfo("linAcc: {}".format(linAcc))
    linAccDict = {'x':linAcc.x, 'y':linAcc.y, 'z':linAcc.z}
    sortedKeys = sorted(linAccDict, key = lambda x: abs(linAccDict[x]))
    maxAxis = sortedKeys[2]
    maxVal = linAccDict[maxAxis]
    #rospy.loginfo("maxAxis: {}, maxVal: {}".format(maxAxis, maxVal))
    
    crashDirection = "none"
    if abs(maxVal) > self.thres:
      rospy.loginfo("Impact detected. maxAxis: {}, maxVal: {}".format(maxAxis, maxVal))
      if maxAxis == 'x':
        rospy.loginfo("  Side impact")
        if maxVal > 0:
          rospy.loginfo("    Left")
          crashDirection = "left"
        else:
          rospy.loginfo("    right")
          crashDirection = "right"
          
      elif maxAxis == 'y':
        rospy.loginfo("  Front/back impact")
        if maxVal > 0:
          rospy.loginfo("    Front")
          crashDirection = "front"
        else:
          rospy.loginfo("    Back")
          crashDirection = "back"
          
      elif maxAxis == 'z':
        rospy.loginfo("  Up/down impact")
        if maxVal > 0:
          rospy.loginfo("    Up")
          crashDirection = "up"
        else:
          rospy.loginfo("    Down")
          crashDirection = "down"
    #else:
      #rospy.loginfo("No collision detected")
    return crashDirection      
          
if __name__ == "__main__":          
  rospy.init_node("CrashReader")
  rate = rospy.Rate(10)
  moveSphero = MoveSphero(0.1, 0.5)
  crashReader = CrashReader(10)
  #rospy.sleep(2)
  
  curDir = "fwd"
  while not rospy.is_shutdown():
    #moveSphero.move(curDir)
    #if curDir == "left" or curDir == "right":
    #  rospy.sleep(2)
    crashDir = crashReader.read()
    if crashDir == "none" and (curDir == "left" or curDir == 'right'):
      curDir = "fwd"
    elif crashDir == "back":
      curDir = "fwd"
    elif crashDir == "front":
      curDir = "back"
    elif crashDir == "left":
      curDir = "right"
    elif crashDir == "right":
      curDir = "left"

    rate.sleep()


  