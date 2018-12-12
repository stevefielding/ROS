from std_srvs.srv import Empty, EmptyResponse, EmptyRequest
glob_local_client = rospy.ServiceProxy('/global_localization', Empty)
crashDetResults = crashDet()
# if crash detected then change direction
if crashDetResults.success == False:
  crashCnt += 1
  rospy.loginfo("Crash detected"
nextDir = crashDetResults.message