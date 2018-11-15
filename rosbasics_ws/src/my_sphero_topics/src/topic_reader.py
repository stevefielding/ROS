#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry

class TopicReader(object):
    
  def __init__(self, topic, msgType):
    print("Starting a TopicReader for: \"{}\"".format(topic))
    self.sub = rospy.Subscriber(topic, msgType, self.callback)
    rospy.wait_for_message(topic, msgType)
    print("TopicReader running")
    self.topicData = None
    
  def callback(self, msg):
    self.topicData = msg
    
  def read(self):
    """
    $ rostopic info /sphero/imu/data3
    Type: sensor_msgs/Imu

    Publishers: 
    * /gazebo (http://10.8.0.1:40401/)
    
    $ rosmsg info sensor_msgs/Imu
    std_msgs/Header header
      uint32 seq
      time stamp
      string frame_id
    geometry_msgs/Quaternion orientation
      float64 x
      float64 y
      float64 z
      float64 w
    float64[9] orientation_covariance
    geometry_msgs/Vector3 angular_velocity
      float64 x
      float64 y
      float64 z
    float64[9] angular_velocity_covariance
    geometry_msgs/Vector3 linear_acceleration
      float64 x
      float64 y
      float64 z
    float64[9] linear_acceleration_covariance
    
    $ rostopic info /odom
    Type: nav_msgs/Odometry

    $ rosmsg info nav_msgs/Odometry
    std_msgs/Header header
      uint32 seq
      time stamp
      string frame_id
    string child_frame_id
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
    geometry_msgs/TwistWithCovariance twist
      geometry_msgs/Twist twist
        geometry_msgs/Vector3 linear
          float64 x
          float64 y
          float64 z
        geometry_msgs/Vector3 angular
          float64 x
          float64 y
          float64 z
      float64[36] covariance
    """
    return self.topicData
   
# ------------------- Test ------------------------ 
if __name__ == '__main__':
  # If you don't declare a node, then the callback is never called
  rospy.init_node('IMUReader')
  rospy.loginfo("Init IMU Reader")
  inertiaMUReader = TopicReader("/sphero/imu/data3", Imu)
  odomReader = TopicReader("/odom", Odometry)
  rospy.sleep(2)
  
  ctrl_c = False
  def shutdown_hook():
    print("Shutting down")
    global ctrl_c
    ctrl_c = True
  
  rospy.on_shutdown(shutdown_hook)
  while ctrl_c == False:
    imuData = inertiaMUReader.read()
    rospy.loginfo("----------- IMU data:\n\"{}\"".format(imuData))
    odomData = odomReader.read()
    rospy.loginfo("----------- odom data:\n\"{}\"".format(odomData))
    rospy.sleep(2)