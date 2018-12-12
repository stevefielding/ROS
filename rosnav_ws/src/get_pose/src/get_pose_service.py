#! /usr/bin/env python

"""
First activate the /amcl_pose topic:
$ roslaunch husky_navigation amcl_demo.launch
Now run this service: 
$ rosrun get_pose get_pose_service.py
Start the telop app:
$ roslaunch husky_navigation_launch keyboard_teleop.launch
Check the results:
$ rosservice call /amcl_pose_service "{}"

rostopic info /amcl_pose
Type: geometry_msgs/PoseWithCovarianceStamped

Publishers:
 * /amcl (http://10.8.0.1:38096/)

Subscribers: None

cat /opt/ros/kinetic/share/geometry_msgs/msg/PoseWithCovarianceStamped.msg
# This expresses an estimated pose with a reference coordinate frame and timestamp

Header header
PoseWithCovariance pose


rosmsg info geometry_msgs/PoseWithCovarianceStamped
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
geometry_msgs/PoseWithCovariance pose
  geometry_msgs/Pose pose
    geometry_msgs/Point position
      float64 x
      float64 y
      float64 z
    geometry_msgs/Quaternion orientation
      float64 x
      float64 y
      float64 z
      float64 w
  float64[36] covariance
  
"""

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_srvs.srv import Empty, EmptyResponse
# cat Trigger.srv
# ---
# bool success   # indicate successful run of triggered service
# string message # informational, e.g. for error messages
from std_srvs.srv import Trigger, TriggerResponse, TriggerRequest

class AmclPoseService(object):
  def __init__(self):
    print("Starting /amcl_pose_service")
    self.poseService = rospy.Service("/amcl_pose_service", Trigger, self.service_callback) 
    self.sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.sub_callback)
    self.topicData = None
    
  def service_callback(self,request):
    response = TriggerResponse()
    response.success = True
    response.message = "x: " + str(self.topicData.pose.pose.position.x) + \
        " ,y: " + str(self.topicData.pose.pose.position.y) + \
        " ,z: " + str(self.topicData.pose.pose.position.z)
    return response
    
    
  def sub_callback(self,msg):
    print("Got /amcl_pose topic data")
    self.topicData = msg

if __name__ == "__main__":
  print("This is get_pose_service")
  rospy.init_node("get_pose_service")
  amclPoseService = AmclPoseService()
  rospy.spin()
