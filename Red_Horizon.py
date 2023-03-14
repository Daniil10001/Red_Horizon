import rospy
from std_msgs.msg import String


rospy.init_node('talker', anonymous=True)
pub = rospy.Publisher('chatter', String, queue_size=10)
rs=rospy.Rate(10) # 10hz

   
if __name__ == '__main__':
    while not rospy.is_shutdown():
         hello_str = "hello world %s" % 1
         rospy.loginfo(hello_str)
         pub.publish(hello_str)
         rs.sleep()