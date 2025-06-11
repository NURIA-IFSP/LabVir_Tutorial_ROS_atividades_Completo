#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Pose2D

# Inicializa o nó ROS
rospy.init_node('goal_publisher', anonymous=True)

# Cria o publisher para o tópico /alvo (supõe que há um nó controlador ouvindo isso)
pub = rospy.Publisher('/alvo', Pose2D, queue_size=10)

rate = rospy.Rate(1)

while not rospy.is_shutdown():
    goal = Pose2D()
    goal.x = float(input("Digite a coordenada X do objetivo: "))
    goal.y = float(input("Digite a coordenada Y do objetivo: "))
    goal.theta = 0.0

    rospy.loginfo("Publicando meta: x=%.2f y=%.2f", goal.x, goal.y)
    pub.publish(goal)
    rate.sleep()