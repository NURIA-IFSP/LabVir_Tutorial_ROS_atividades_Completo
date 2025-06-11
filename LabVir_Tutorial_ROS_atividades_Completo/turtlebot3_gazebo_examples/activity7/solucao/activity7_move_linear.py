#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

def move_forward():
    rospy.init_node('move_turtlebot3_forward')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel = Twist()

    # Define a velocidade linear e angular
    vel.linear.x = 0.2  # Avança devagar
    vel.angular.z = 0.0

    # Tempo de execução
    duration = rospy.Duration(5)  # 5 segundos

    rospy.loginfo("Movendo o TurtleBot3 para frente por 5 segundos")
    start_time = rospy.Time.now()

    rate = rospy.Rate(10)
    while rospy.Time.now() - start_time < duration:
        pub.publish(vel)
        rate.sleep()

    # Para o robô
    vel.linear.x = 0.0
    pub.publish(vel)
    rospy.loginfo("Parando o TurtleBot3")

if __name__ == '__main__':
    try:
        move_forward()
    except rospy.ROSInterruptException:
        pass