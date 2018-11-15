#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node('start_bb8_square_move')
print("Waiting for /bb8_service to start")
rospy.wait_for_service('/bb8_service')

req = EmptyRequest()
bb8_move_square_service = rospy.ServiceProxy('/bb8_service', Empty)
print("Requesting BB8 move in square")
bb8_move_square_service(req)
print("completed move in square")

