#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
import time

# Inicializa o nó ROS
rospy.init_node('move_square')

# Cria o publisher para o tópico /turtle1/cmd_vel
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

# Define a mensagem de velocidade
vel = Twist()
vel.linear.x = 2.0   # Velocidade linear
vel.angular.z = 0.0  # Sem rotação

# Tempo de execução de cada lado do quadrado
side_duration = 3.0

# Frequência de publicação
rate = rospy.Rate(1)

for i in range(5):
    # Move em linha reta
    rospy.loginfo("Movendo para frente")
    vel.linear.x = 2.0
    vel.angular.z = 0.0
    pub.publish(vel)
    time.sleep(side_duration)

    # Gira 90 graus
    rospy.loginfo("Girando 90 graus")
    vel.linear.x = 0.0
    vel.angular.z = 1.57  # Aproximadamente 90 graus/seg
    pub.publish(vel)
    time.sleep(1.0)

# Para a tartaruga
vel.linear.x = 0.0
vel.angular.z = 0.0
pub.publish(vel)
