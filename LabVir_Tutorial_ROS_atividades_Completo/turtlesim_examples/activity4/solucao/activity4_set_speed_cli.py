#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from custom_msgs.srv import SetSpeed

# Inicializa o nó
rospy.init_node('set_speed_client')

# Aguarda o serviço estar disponível
rospy.wait_for_service('set_speed')

try:
    set_speed = rospy.ServiceProxy('set_speed', SetSpeed)
    vel = float(input("Digite a nova velocidade: "))
    resp = set_speed(vel)
    if resp.success:
        rospy.loginfo("Velocidade atualizada com sucesso!")
    else:
        rospy.logwarn("Falha ao atualizar velocidade.")
except rospy.ServiceException as e:
    rospy.logerr("Erro ao chamar serviço: %s", e)