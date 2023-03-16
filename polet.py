import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import PoseStamped, Point, Quaternion,Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from visualization_msgs.msg import MarkerArray,Marker

tf_buffer = tf2_ros.Buffer()  # tf buffer length
tf_listener = tf2_ros.TransformListener(tf_buffer)

def pose(tr="aruco_map"):
    #print(rospy.Time.now())
    transform = tf_buffer.lookup_transform(tr, 'body', rospy.Time(rospy.Time.now().to_sec()-0.05))
    #print(transform)
    q=quaternion_from_euler(0,0,0)
    pose_transformed = tf2_geometry_msgs.do_transform_pose(PoseStamped(pose=Pose(position=Point(0,0,0), orientation=Quaternion(*q))), transform)
    #print(0)
    q=pose_transformed.pose.orientation
    p=pose_transformed.pose.position
    return p.x,p.y,p.z

nav=[]

def poisk(data):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img= cv2.inRange(img, (0,19,114), (59,95,255))
    imgl=img[img.shape[0]//2-1:img.shape[0]//2+1,0:int(img.shape[1]*0.375)]
    imgr=img[img.shape[0]//2-1:img.shape[0]//2+1,int(img.shape[1]*(1-0.375)):img.shape[1]]
    imgvr=img[0:int(img.shape[0]*0.3), img.shape[1]//2-1:img.shape[1]//2+1]
    imgvn=img[int(img.shape[0]*(1-0.3)):img.shape[0], img.shape[1]//2-1:img.shape[1]//2+1]
    pl,pr,pvr,pvn=cv2.moments(imgl)['m00']/(imgl.shape[0]*imgl.shape[1]*255),cv2.moments(imgr)['m00']/(imgr.shape[0]*imgr.shape[1]*255), \
              cv2.moments(imgvr)['m00']/(imgvr.shape[0]*imgvr.shape[1]*255),cv2.moments(imgvn)['m00']/(imgvn.shape[0]*imgvn.shape[1]*255)
    x,y,z=pose(tr="aruco_map")
    if (pvr>80):
        if (y+0.1<4.1):
            nav.append([x,y+0.1])
    elif (pr>80):
        if (x+0.1<7.1):
            nav.append([x+0.1,y])
    else:
        nav.append([x,y-0.1])