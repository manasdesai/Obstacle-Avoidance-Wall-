#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
def callback(msg):
    if msg.ranges[360]>1:
        move.linear.x=.5
        move.angular.z=0.0
    if msg.ranges[360]<1:
        move.linear.x=0
        move.angular.z=0
    pub.publish(move)
    
rospy.init_node('moverobot')
pub=rospy.Publisher('cmd_vel',Twist,queue_size=1)
sub=rospy.Subscriber('/scan',LaserScan,callback)
move=Twist()

rospy.spin()
