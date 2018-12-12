#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse, EmptyRequest

class Init_particles(object):
  def __init__(self):
    rospy.loginfo("Waiting for /global_localization")
    rospy.wait_for_service('/global_localization')
    try:
      self.glob_local_client = rospy.ServiceProxy('/global_localization', Empty)
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
  
  def init(self):
    req = EmptyRequest()
    results = self.glob_local_client(req)
    rospy.loginfo("init_particles: {}".format(results))

if __name__ == "__main__":
  rospy.init_node("init_particles")
  init_particles = Init_particles()
  init_particles.init()
  