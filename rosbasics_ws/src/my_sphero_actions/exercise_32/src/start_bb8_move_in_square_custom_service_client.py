#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node('start_bb8_square_move')
print("Waiting for /bb8service to start")
rospy.wait_for_service('/move_bb8_in_square_custom')

req = MyCustomServiceMessageRequest()
req.radius = 0.1
req.repetitions = 2
bb8_move_custom_square_service = rospy.ServiceProxy('/move_bb8_in_square_custom', MyCustomServiceMessage)
print("Requesting BB8 move in custom square")
result1 = bb8_move_custom_square_service(req)
req.radius = 0.3
req.repetitions = 1
result2 = bb8_move_custom_square_service(req)
if result1.success ==  False or result2.success == False:
  print("Move failed")
else:
  print("Successfully completed the move")

