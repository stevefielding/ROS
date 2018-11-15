#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse # you import the service message python classes 
from move_bb8 import MoveBB8

def move_callback(request):
    #print ("move_callback has been called")
    print "Request Data==> radius="+str(request.radius)+", repetitions = "+str(request.repetitions)
    response = MyCustomServiceMessageResponse()
    if request.radius > 1 or request.radius == 0.0 or request.repetitions < 1 or request.repetitions > 10:  
      response.success = False
      print("Bad arguements. Either radius or repetitions is out of range")
      return response
    for i in range(request.repetitions):
      moveBB8.move_square(request.radius)
    #print("move complete")
    response.success = True
    return response

rospy.init_node('service_server') 
#rate = rospy.Rate(4)
moveBB8 = MoveBB8()
print("Starting bb8_service")
bb8_service = rospy.Service('/move_bb8_in_square_custom', MyCustomServiceMessage , move_callback) # create the Service called my_service with the defined callback
rospy.spin() # mantain the service open.