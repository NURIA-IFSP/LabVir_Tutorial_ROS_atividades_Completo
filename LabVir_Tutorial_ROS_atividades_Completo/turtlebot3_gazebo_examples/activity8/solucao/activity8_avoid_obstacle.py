#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoider:
    def __init__(self):
        rospy.init_node('turtlebot3_avoid_obstacles')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.cmd = Twist()
        rospy.spin()

    def scan_callback(self, msg):
        front = msg.ranges[len(msg.ranges) // 2]  # Ponto central

        if front < 0.4:
            # Obstáculo à frente: gira
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = 0.5
        else:
            # Sem obstáculo: avança
            self.cmd.linear.x = 0.2
            self.cmd.angular.z = 0.0

        self.pub.publish(self.cmd)

if __name__ == '__main__':
    try:
        ObstacleAvoider()
    except rospy.ROSInterruptException:
        pass