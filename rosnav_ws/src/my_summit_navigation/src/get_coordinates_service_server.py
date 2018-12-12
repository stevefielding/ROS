#! /usr/bin/env python

import rospy
import yaml
from my_summit_navigation.srv import pathPlanMessage, pathPlanMessageResponse
from geometry_msgs.msg import PoseWithCovarianceStamped
from send_coordinates_action_client import SendCoords

class PathPlanServiceServer(object):
    
  def __init__(self, fileName):
    self.spotService = rospy.Service('/get_spot', pathPlanMessage , self.service_callback)
    rospy.loginfo("[INFO] using spot file: {}".format(fileName))
    self.fileName = fileName

  def service_callback(self, request):
    print ("Request label: {}".format(request.label))
    my_response = pathPlanMessageResponse()

    try:
      print("Attempting to read file")
      file = open(self.fileName, "r")
      print("File opened")
      pose = file.read()
      print("File loaded using yaml")
      file.close()
      #print(pose)
      print("File closed")
    except:
      my_response.navigation_successfull = False
      my_response.message = "Failed to read pose from file: {}".format(self.fileName)
      return my_response
 
    sendcoords = SendCoords()
    status = sendcoords.sendGoal(pose, request.label)
    my_response.navigation_successfull = status
    my_response.message = "We're done"   
    return  my_response # the service Response class, in this case MyServiceMessageResponse

if __name__ == "__main__":
  rospy.init_node('pathPlanServiceServer')
  pathPlanServiceServer = PathPlanServiceServer("/home/user/catkin_ws/src/my_summit_navigation/spot.yaml")
  rospy.spin() # mantain the service open.  
