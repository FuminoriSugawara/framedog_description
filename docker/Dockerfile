# RViz + joint_state_publisher_gui environment for framedog_description.
# BASE_IMAGE defaults to a locally-present jazzy desktop image (no pull needed);
# override with e.g. --build-arg BASE_IMAGE=osrf/ros:humble-desktop.
ARG BASE_IMAGE=osrf/ros:jazzy-desktop-full
FROM ${BASE_IMAGE}
ARG ROS_DISTRO=jazzy

# rviz2 / robot_state_publisher come with the -desktop image;
# add xacro and the joint_state_publisher GUI.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ros-${ROS_DISTRO}-xacro \
        ros-${ROS_DISTRO}-joint-state-publisher-gui \
    && rm -rf /var/lib/apt/lists/*

ENV ROS_DISTRO=${ROS_DISTRO}
WORKDIR /ws

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["ros2", "launch", "framedog_description", "display.launch.py"]
