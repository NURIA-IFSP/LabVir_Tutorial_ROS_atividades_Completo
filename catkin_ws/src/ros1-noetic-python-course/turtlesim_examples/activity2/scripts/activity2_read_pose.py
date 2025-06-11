#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from turtlesim.msg import Pose

def pose_callback(msg):
    rospy.loginfo("Posição atual:")
    rospy.loginfo("x = %.2f, y = %.2f, theta = %.2f", msg.x, msg.y, msg.theta)

# Inicializa o nó ROS
rospy.init_node('read_pose', anonymous=True)

# Cria o subscriber para o tópico /turtle1/pose
rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

# Mantém o nó ativo
rospy.spin()