#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def send_goal(x, y):
    rospy.init_node('turtlebot3_movebase_client')
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    # Define a meta
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'  # Usa o frame do mapa
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo("Enviando meta: x=%.2f y=%.2f", x, y)
    client.send_goal(goal)
    client.wait_for_result()

    rospy.loginfo("Meta alcançada? %s", client.get_result())

if __name__ == '__main__':
    try:
        x = float(input("Digite a coordenada X da meta: "))
        y = float(input("Digite a coordenada Y da meta: "))
        send_goal(x, y)
    except rospy.ROSInterruptException:
        pass

