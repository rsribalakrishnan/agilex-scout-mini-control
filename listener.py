#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
import pyagxrobots
import time
import sys
import signal


def signal_handler(signal, frame):
    print('Pressed Ctrl + C!')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

current_twist = Twist()
scoutmini = pyagxrobots.pysdkugv.ScoutMiniBase()
scoutmini.EnableCAN()

def callback(data):
    global current_twist
    current_twist = data

    rospy.loginfo(rospy.get_caller_id() + 'Received data')
    scout_msg = repr(f'Twist Msg: (Move={data.linear.x}, Turn={data.angular.z})')
    # se.write(scout_msg + "\n")

    print(current_twist.linear.x, current_twist.angular.z)
    scoutmini.SetMotionCommand(linear_vel=current_twist.linear.x)



def listener():
    rospy.init_node('scout_controller', anonymous=True)
    velocity_subscriber = rospy.Subscriber('/cmd_vel', Twist, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
    
