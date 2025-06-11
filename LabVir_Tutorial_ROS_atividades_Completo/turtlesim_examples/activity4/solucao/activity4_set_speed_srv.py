#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
from turtlesim.srv import SetPen
from custom_msgs.srv import SetSpeed, SetSpeedResponse

# Callback do serviço
def handle_set_speed(req):
    rospy.loginfo("Recebida nova velocidade: %.2f", req.speed)
    pub.publish(req.speed)
    return SetSpeedResponse(success=True)

# Inicializa o nó
rospy.init_node('set_speed_server')

# Publisher para o controle de velocidade
pub = rospy.Publisher('/velocidade', Float32, queue_size=10)

# Cria o servidor do serviço
srv = rospy.Service('set_speed', SetSpeed, handle_set_speed)

rospy.loginfo("Servidor de velocidade pronto")
rospy.spin()