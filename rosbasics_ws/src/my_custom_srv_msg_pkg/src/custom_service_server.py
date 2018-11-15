#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse # you import the service message python classes 
                                                                                         # generated from MyCustomServiceMessage.srv.


def my_callback(request):
    
    print "Request Data==> radius="+str(request.radius)+", repetitions = "+str(request.repetitions)
    my_response = MyCustomServiceMessageResponse()
    if request.radius > 5.0:
        my_response.success = True
    else:
        my_response.success = False
    return  my_response # the service Response class, in this case MyCustomServiceMessageResponse

rospy.init_node('service_client') 
my_service = rospy.Service('/my_service', MyCustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # mantain the service open.
