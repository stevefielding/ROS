#! /usr/bin/env python

import rospy
from spot_recorder.srv import MyServiceMessage, MyServiceMessageResponse
from geometry_msgs.msg import PoseWithCovarianceStamped

class SpotServiceServer(object):
    
  def __init__(self, fileName):
    self.spotService = rospy.Service('/record_spot', MyServiceMessage , self.service_callback)
    self.sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.sub_callback)
    self.fileName = fileName
    self.pose = None
    self.poseSave = ""
    
  def service_callback(self, request):
    print ("Request label: {}".format(request.label))
    my_response = MyServiceMessageResponse()
    # check if pose data has been updated by the sub_callback
    if self.pose == None:
      rospy.loginfo("[ERROR] Have you started amcl node?")
      my_response.navigation_successfull = False
      my_response.message = "No pose info received. Have you started amcl node?"

    # pose data is available, so process
    else:

      # if "end" requested, then save all the accumulated labels and pose data to file
      if request.label == "end":
        try:
          file = open(self.fileName, "a+")
          file.write(self.poseSave + "\n")
          file.close()
          my_response.navigation_successfull = True
          my_response.message = "Pose saved to file: {}".format(self.fileName)
        except:
          my_response.navigation_successfull = False
          my_response.message = "Failed to save pose to file: {}".format(self.fileName)

      # else append the label and pose data as a string
      else:
        my_response.navigation_successfull = True
        my_response.message = "Pose updated: {}".format(request.label)
        self.poseSave += "label: " + request.label + "\n"
        self.poseSave += str(self.pose.pose.pose) + "\n\n"

    return  my_response # the service Response class, in this case MyServiceMessageResponse

  def sub_callback(self, msg):
    self.pose = msg
    
if __name__ == "__main__":
  rospy.init_node('spotServiceServer')
  spotServiceServer = SpotServiceServer("/home/user/spot.yaml")
  rospy.spin() # mantain the service open.  
