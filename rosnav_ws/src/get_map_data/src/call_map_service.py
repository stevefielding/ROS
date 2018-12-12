#! /usr/bin/env python

"""
rosservice info /static_map
Node: /my_map_server
URI: rosrpc://10.8.0.1:37817
Type: nav_msgs/GetMap
Args:

roscd nav_msgs/
user:/opt/ros/kinetic/share/nav_msgs$ cd srv
cat GetMap.srv
# Get the map as a nav_msgs/OccupancyGrid
---
nav_msgs/OccupancyGrid map



rosmsg info nav_msgs/OccupancyGrid
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
nav_msgs/MapMetaData info
  time map_load_time
  float32 resolution
  uint32 width
  uint32 height
  geometry_msgs/Pose origin
    geometry_msgs/Point position
      float64 x
      float64 y
      float64 z
    geometry_msgs/Quaternion orientation
      float64 x
      float64 y
      float64 z
      float64 w
int8[] data




rossrv info nav_msgs/GetMap
---
nav_msgs/OccupancyGrid map
  std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
  nav_msgs/MapMetaData info
    time map_load_time
    float32 resolution
    uint32 width
    uint32 height
    geometry_msgs/Pose origin
      geometry_msgs/Point position
        float64 x
        float64 y
        float64 z
      geometry_msgs/Quaternion orientation
        float64 x
        float64 y
        float64 z
        float64 w
  int8[] data
"""

import rospy
from nav_msgs.srv import GetMap, GetMapRequest

rospy.init_node("get_my_map")
rospy.loginfo("Waiting for /static_map service to start...")
rospy.wait_for_service("/static_map")
try:
  getMapClient = rospy.ServiceProxy("/static_map", GetMap)
except rospy.ServiceException, e:
  print("Serice call failed {}".format(e))
  
req = GetMapRequest()
results = getMapClient(req)
print("Resolution: {}".format(results.map.info.resolution))
print("w: {}, h {}".format(results.map.info.width, results.map.info.height))

