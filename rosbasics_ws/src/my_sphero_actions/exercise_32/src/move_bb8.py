import rospy
from geometry_msgs.msg import Twist 
#from exercise_22.msg import Prox
from std_msgs.msg import String
from nav_msgs.msg import Odometry
import math


class MoveBB8:

  def __init__(self):
    self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    #self.pubText = rospy.Publisher('chatter', String, queue_size=10)
    self.twist = Twist()
    #self.sub = rospy.Subscriber('odom', Odometry, self.callback)

  #def callback(self, msg):
    #print(msg.pose.pose)
    #self.pose = msg.pose.pose.position
    
  def moveFwd(self, x):
    self.twist.linear.x = x
    self.pub.publish(self.twist)
    #while math.sqroot(self.pose.x ** 2 + self.pose.y ** 2) < tgt:
    #  pass
    #self.twist.linear.x = 0
    #self.pubText.publish("The time is {}".format(rospy.get_time()))
 
  def turn(self, z):
    self.twist.angular.z = z
    self.pub.publish(self.twist)
    #self.pubText.publish("The time is {}".format(rospy.get_time()))
    
  def moveStraightThenTurn(self, fwdVel):
    self.moveFwd(fwdVel)
    rospy.sleep(4)
    self.moveFwd(0.0)
    rospy.sleep(2)
    self.turn(0.19)
    rospy.sleep(4)
    self.turn(0.0)
    rospy.sleep(1)
    
  def move_square(self, fwdVel):
    self.moveStraightThenTurn(fwdVel)
    self.moveStraightThenTurn(fwdVel)
    self.moveStraightThenTurn(fwdVel)
    self.moveStraightThenTurn(fwdVel)

