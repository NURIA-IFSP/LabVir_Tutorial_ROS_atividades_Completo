# ROS1 Noetic Python Course - Estrutura Inicial com Soluções Comentadas

Este repositório contém um conjunto de atividades práticas para o aprendizado de conceitos fundamentais do ROS1 Noetic utilizando Python. As atividades foram pensadas para facilitar a visualização e o entendimento dos conceitos através de simulações com `turtlesim` e `TurtleBot3` no Gazebo.

## 🗂️ Estrutura de diretórios esperada:

```bash
ros1-noetic-python-course/
├── CMakeLists.txt
├── package.xml
├── turtlesim_examples/
│   ├── activity1/
│   │   ├── enunciado.md
│   │   └── solucao/
│   │       └── activity1_move_square.py
│   ├── activity2/
│   │   ├── enunciado.md
│   │   └── solucao/
│   │       └── activity2_read_pose.py
│   ├── activity3/
│   │   ├── enunciado.md
│   │   └── solucao/
│   │       └── activity3_goal_publisher.py
│   ├── activity4/
│   │   ├── enunciado.md
│   │   ├── solucao/
│   │   │   ├── activity4_set_speed_srv.py
│   │   │   └── activity4_set_speed_cli.py
│   │   └── srv/
│   │       └── SetSpeed.srv
├── turtlebot3_gazebo_examples/
│   ├── activity5/
│   │   ├── enunciado.md
│   │   └── solucao/
│   │       └── teleop_instructions.md
│   ├── activity7/
│   │   ├── enunciado.md
│   │   └── solucao/
│   │       └── activity7_move_linear.py
│   ├── activity8/
│   │   ├── enunciado.md
│   │   └── solucao/
│   │       └── activity8_avoid_obstacle.py
│   ├── activity9/
│   │   ├── enunciado.md
│   │   └── solucao/
│   │       └── rviz_setup.launch
│   └── activity10/
│       ├── enunciado.md
│       └── solucao/
│           └── activity10_move_base_client.py
```

## 📚 Como utilizar este repositório

1. Clone este repositório dentro do seu `catkin_ws/src`:
```bash
cd ~/catkin_ws/src
git clone <url_do_repositorio>
```

2. Compile seu workspace:
```bash
cd ~/catkin_ws
catkin_make
```

3. Ative o ambiente:
```bash
source devel/setup.bash
```

4. Navegue até a atividade desejada e siga as instruções contidas no `enunciado.md`.

## 💡 Dicas importantes

- Cada atividade contém um arquivo de enunciado e uma pasta `solucao` com o código comentado para estudo.
- Utilize o `rqt_graph`, `rostopic`, `rosnode` e `rosservice` para investigar a comunicação entre nós.
- Para atividades com TurtleBot3 no Gazebo, é necessário ter o pacote `turtlebot3_gazebo` instalado e corretamente configurado com o modelo exportado:
```bash
export TURTLEBOT3_MODEL=burger
```

## 📦 Dependências necessárias

- ROS Noetic
- turtlesim
- turtlebot3
- gazebo_ros
- teleop_twist_keyboard

---

Este conjunto de atividades foi desenvolvido como parte do curso prático de ROS1 com Python no LabVir (IFSP).