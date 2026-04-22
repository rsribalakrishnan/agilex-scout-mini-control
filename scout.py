#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import rospy
import roslib
import subprocess
import time
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
import sys
import signal


def signal_handler(signal, frame):
    print('Pressed Ctrl + C!')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


class robot:

    def __init__(self):
        rospy.init_node('xbox_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist,
                queue_size=1)
        self.joy_subscriber = rospy.Subscriber('/joy', Joy,
                self.callback)
        self.rate = rospy.Rate(20)  # 20hz

    def callback(self, data):
        global inn
        inn = 0
        self.buttons = data.buttons
        self.axes = data.axes
        if np.shape(self.buttons)[0] > 0:
            inn = 1
            self.a = self.buttons[0]
            self.b = self.buttons[1]
            self.x = self.buttons[2]
            self.y = self.buttons[3]

        if np.shape(self.axes)[0] > 0:
            inn = 1
            self.linear = self.axes[1]
            self.angular = self.axes[0]
        if inn == 1:
            if self.buttons[0] == 0 and self.buttons[1] == 0 \
                and self.buttons[2] == 0 and self.buttons[3] == 0 \
                and self.axes[0] == 0 and self.axes[1] == 0:
                inn = 0
            else:
                pass

    def moving(self, vel_msg):
        self.velocity_publisher.publish(vel_msg)


data = Joy()
vel_msg = Twist()

scout = robot()
scout.callback(data)

global inn
inn = 0

if __name__ == '__main__':
    while 1:
        if inn == 1:
            if scout.a == 1:
                vel_msg.linear.x = scout.linear + 0.4
                vel_msg.angular.z = scout.angular + 1.2
            elif scout.b == 1:
                p = \
                    subprocess.Popen('rostopic pub /reset std_msgs/Empty "{}"'
                        , shell=True)
                time.sleep(2)
                p.terminate()
            elif scout.x == 1:
                vel_msg.linear.x = scout.linear + 0.8
                vel_msg.angular.z = scout.angular + 2
            elif scout.y == 1:
                vel_msg.linear.x = 0
                vel_msg.angular.z = 0
            scout.moving(vel_msg)
        else:
            print('No data in!')
        scout.rate.sleep()

