#! /usr/bin/env python

import rospy
from std_msgs.msg import String
import rospkg
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest

rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
req = ExecTrajRequest()
req.file = traj
print(traj)

rospy.init_node('service_client') # Initialise a ROS node with the name service_client
print("Waiting for service to start")
rospy.wait_for_service('/execute_trajectory') # Wait for the service client /iri_wam_reproduce_trajectory/ExecTraj to be running
print("Create service proxy")
exec_traj_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj) # Create the connection to the service
print("Execute trajectory")
result = exec_traj_service(req) # Send through the connection the filename of the file containing the trajectory
print result # Print the result given by the service called
print("Finished exercise_3_1.py")