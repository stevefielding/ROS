#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from move_bb8 import MoveBB8

def move_callback(request):
    print ("move_callback has been called")
    moveBB8.move_square(0.7)
    print("move complete")
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('service_server') 
#rate = rospy.Rate(4)
moveBB8 = MoveBB8()
print("Starting bb8_service")
bb8_service = rospy.Service('/bb8_service', Empty , move_callback) # create the Service called my_service with the defined callback
rospy.spin() # mantain the service open.