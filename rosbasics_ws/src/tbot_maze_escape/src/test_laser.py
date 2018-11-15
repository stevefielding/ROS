#! /usr/bin/env python
# rosun tbot_maze_escape test_laser
# To move turtlebot:    roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

import rospy
from geometry_msgs.msg import Twist

#rostopic info /kobuki/laser/scan
#Type: sensor_msgs/LaserScan
from sensor_msgs.msg import LaserScan

#rostopic info /odom
#Type: nav_msgs/Odometry
from nav_msgs.msg import Odometry

class TestLaser(object):
  
  def __init__(self):
    self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    self.laser_sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.laser_callback)
    rospy.loginfo("Waiting for \"/kobuki/laser/scan\"")
    rospy.wait_for_message('/kobuki/laser/scan', LaserScan)
    self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
    rospy.loginfo("Waiting for \"/odom\"")
    rospy.wait_for_message('/odom', Odometry)
    
  def pubOnce(self,cmd):
    num_connections = self.pub.get_num_connections()
    while num_connections == 0:
      num_connections = self.pub.get_num_connections()
    self.pub.publish(cmd)

  def laser_callback(self, msg):
    self.laser_topicData = msg
  
  def odom_callback(self, msg):
    self.odom_topicData = msg

if __name__ == "__main__":
  rospy.init_node("test_laser")
  testLaser = TestLaser()
  twist = Twist()
  twist.linear.x = 1.0
  twist.angular.z = 0.0
  #testLaser.pubOnce(twist)
  rate = rospy.Rate(1)
  dispEn_laser = False
  dispEn_pos = True
  dispEn_orient = False
  dispEn_linear = False
  dispEn_ang = False
  while not rospy.is_shutdown():
    
    # read laser ranges
    # Regular Cartesian co-ordinates
    # When tbot front has collided with object, rangeAhead = 0.17 to 0.20
    myLen = len(testLaser.laser_topicData.ranges)
    rangeAhead = testLaser.laser_topicData.ranges[int(myLen/2)]
    rangeLeft = testLaser.laser_topicData.ranges[-1]
    rangeRight = testLaser.laser_topicData.ranges[0]
    if dispEn_laser == True:
      print("Ahead: {}, Left: {}, Right {}".format(rangeAhead, rangeLeft, rangeRight))
    
    # read odom position
    # y positive is down, y negative is up
    # x positive is left, x negative is left
    # Regular Cartesian co-ordinates
    pos_x = testLaser.odom_topicData.pose.pose.position.x
    pos_y = testLaser.odom_topicData.pose.pose.position.y
    pos_z = testLaser.odom_topicData.pose.pose.position.z
    if dispEn_pos == True:
      print("Position x: {}, y {}, z {}".format(pos_x, pos_y, pos_z))
    
    # read odom orientation
    # As tbot is rotated, x and y do not vary, but z varies
    # z is always 0 when tbot is pointing left, and is either +1 or -1 when tbot is pointing right
    # This looks like quaternians
    orient_x = testLaser.odom_topicData.pose.pose.orientation.x
    orient_y = testLaser.odom_topicData.pose.pose.orientation.y
    orient_z = testLaser.odom_topicData.pose.pose.orientation.z
    orient_w = testLaser.odom_topicData.pose.pose.orientation.w
    if dispEn_orient == True:
      print("Orientation x: {}, y {}, z {}".format(orient_x, orient_y, orient_z))

    # Read odom linear
    # y and z never vary.
    # x denotes the linear velocity. Positive is forward and negative is backward
    linear_x = testLaser.odom_topicData.twist.twist.linear.x
    linear_y = testLaser.odom_topicData.twist.twist.linear.y
    linear_z = testLaser.odom_topicData.twist.twist.linear.z
    if dispEn_linear == True:
      print("Linear x: {}, y {}, z {}".format(linear_x, linear_y, linear_z))

    # Read odom angular
    # x and y don't vary. Only z varies
    # z positive is clockwise, z negative is anti-clockwise
    ang_x = testLaser.odom_topicData.twist.twist.angular.x
    ang_y = testLaser.odom_topicData.twist.twist.angular.y
    ang_z = testLaser.odom_topicData.twist.twist.angular.z
    if dispEn_ang == True:
      print("Angular x: {}, y {}, z {}".format(ang_x, ang_y, ang_z))
    
    rate.sleep()
  rospy.spin()
