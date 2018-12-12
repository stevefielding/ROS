#! /usr/bin/env python
"""
rosservice info /move_base/make_plan
Node: /move_base
URI: rosrpc://10.8.0.1:43516
Type: nav_msgs/GetPlan
Args: start goal tolerance

rossrv show nav_msgs/GetPlan
geometry_msgs/PoseStamped start
  std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
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
geometry_msgs/PoseStamped goal
  std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
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
float32 tolerance
---
nav_msgs/Path plan
  std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
  geometry_msgs/PoseStamped[] poses
    std_msgs/Header header
      uint32 seq
      time stamp
      string frame_id
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

"""

import rospy
from nav_msgs.srv import GetPlan, GetPlanRequest

rospy.init_node("make_plan")
print("Waiting for /move_base/make_plan service")
rospy.wait_for_service('/move_base/make_plan')
try:
  makePlanClient = rospy.ServiceProxy('/move_base/make_plan', GetPlan)
except rospy.ServiceException, e:
  print "Service call failed: %s"%e

req = GetPlanRequest()

# Start
req.start.header.frame_id = 'map'
req.start.pose.orientation.z = 0.7071
req.start.pose.orientation.w = 0.7071

# goal
req.goal.header.frame_id = 'map'
req.goal.pose.position.x = 1.0
req.goal.pose.position.y = 1.0
req.goal.pose.orientation.z = 0.7071
req.goal.pose.orientation.w = 0.7071

print(req)

results = makePlanClient(req)
rospy.loginfo("Results: {}".format(results))
