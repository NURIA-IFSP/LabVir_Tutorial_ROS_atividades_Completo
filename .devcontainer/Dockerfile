FROM osrf/ros:noetic-desktop-full

# Argumentos para criar usuário não-root
ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV DEBIAN_FRONTEND=noninteractive

# === INSTALA FERRAMENTAS BÁSICAS E REMOVE REPOSITÓRIO ANTIGO DO ROS ===
RUN sed -i '/packages.ros.org/d' /etc/apt/sources.list.d/ros1-latest.list \
    && apt-get update \
    && apt-get install -y curl wget gnupg2 lsb-release ca-certificates sudo

# === INSTALA NOVA CHAVE GPG DO ROS ===
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc \
    | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg

# === RECONFIGURA O REPOSITÓRIO DO ROS ===
RUN echo "deb [signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" \
    > /etc/apt/sources.list.d/ros1-latest.list

# === CRIA USUÁRIO ===
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    usermod -aG sudo,dialout,video $USERNAME && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

# Alterna para o novo usuário
USER $USERNAME

# Adiciona ao grupo video
# RUN sudo usermod --append --groups video $USERNAME

# Atualiza pacotes e instala dependências ROS
RUN sudo apt update && sudo apt upgrade -y && \
    sudo apt install -y git nano python-is-python3 \
    ros-noetic-ros-tutorials \
    ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control \
    liburdfdom-tools \
    ros-noetic-effort-controllers \
    ros-noetic-ros-control ros-noetic-ros-controllers \
    python3-catkin-tools \
    ros-noetic-moveit

# Atualiza rosdep
RUN sudo rosdep update

# Volta para root para instalar ambiente gráfico
USER root

# === INSTALA XFCE + VNC ===
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    xfce4 xfce4-terminal \
    novnc websockify xterm x11vnc net-tools \
    python3-pip libgl1-mesa-dri libgl1-mesa-glx dbus-x11 mesa-utils \
    x11-utils x11-xserver-utils wmctrl xdotool firefox autocutsel && \
    apt-get clean

# Configura o display correto para o ambiente gráfico
ENV DISPLAY=:1

# === DESABILITA AVISO DE EOL DO ROS ===
ENV DISABLE_ROS1_EOL_WARNINGS=1


# Instala dependências para o VSCode
RUN apt-get update && apt-get install -y \
    gnome-keyring \
    libsecret-1-0 libsecret-1-dev

# Instala TurboVNC
RUN wget -O /tmp/turbovnc.deb https://github.com/TurboVNC/turbovnc/releases/download/3.1.1/turbovnc_3.1.1_amd64.deb && \
    dpkg -i /tmp/turbovnc.deb || apt-get install -fy && \
    rm /tmp/turbovnc.deb

# Adiciona TurboVNC ao PATH
ENV PATH="/opt/TurboVNC/bin:${PATH}"

# Instala o VSCode
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list && \
    apt update && apt install -y code

# Configura VNC com senha fixa
RUN mkdir -p /home/${USERNAME}/.vnc && \
    echo "senha-segura" | /opt/TurboVNC/bin/vncpasswd -f > /home/${USERNAME}/.vnc/passwd && \
    chmod 600 /home/${USERNAME}/.vnc/passwd && \
    chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}/.vnc

# Copia scripts
COPY scripts/*.sh /home/${USERNAME}/
RUN chown ${USERNAME}:${USERNAME} /home/${USERNAME}/start-*.sh && \
    chmod +x /home/${USERNAME}/start-*.sh



# Configura ROS no .bashrc
RUN echo "source /opt/ros/noetic/setup.bash" >> /home/$USERNAME/.bashrc && \
    echo "source /projeto1_PosDoc/init.bash" >> /home/$USERNAME/.bashrc && \
    chown $USERNAME:$USERNAME /home/$USERNAME/.bashrc

# === COPIA O WORKSPACE ===
#  COPY catkin_ws /home/$USERNAME/catkin_ws

# Copia o curso para o catkin_ws/src
COPY ../LabVir_Tutorial_ROS_atividades_Completo /home/${USERNAME}/catkin_ws/src/ros1-noetic-python-course


# Compila o workspace
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && cd /home/${USERNAME}/catkin_ws && catkin_make"

# Configura ROS no bashrc
RUN echo "source /opt/ros/noetic/setup.bash" >> /home/$USERNAME/.bashrc && \
    echo "source /home/$USERNAME/catkin_ws/devel/setup.bash" >> /home/$USERNAME/.bashrc && \
    chown $USERNAME:$USERNAME /home/$USERNAME/.bashrc


RUN echo "source /home/$USERNAME/catkin_ws/devel/setup.bash" >> /home/$USERNAME/.bashrc && \
    sudo chown -R $USERNAME:$USERNAME /home/$USERNAME/catkin_ws

# === WALLPAPER ===
COPY images/wallpapers/ /usr/share/backgrounds/labvir/
RUN chmod 644 /usr/share/backgrounds/labvir/*

USER $USERNAME
RUN mkdir -p /home/$USERNAME/.config/autostart && \
    echo "[Desktop Entry]\n\
Type=Application\n\
Name=Set Wallpaper\n\
Exec=/home/ubuntu/set-wallpaper.sh\n\
Terminal=false\n\
X-GNOME-Autostart-enabled=true" \
> /home/$USERNAME/.config/autostart/set-wallpaper.desktop && \
chmod +x /home/$USERNAME/.config/autostart/set-wallpaper.desktop

# === INSTALA ROS-APT-SOURCE (MANTÉM AS CHAVES ATUALIZADAS) ===
USER root
RUN apt update && apt install -y ros-apt-source
    
# Alterna para usuário não-root
USER $USERNAME

# Expõe portas
EXPOSE 5901 6080
# Comando padrão
CMD ["/home/ubuntu/start-vnc.sh"]
