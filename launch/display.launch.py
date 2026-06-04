import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg = "framedog_description"
    pkg_share = get_package_share_directory(pkg)

    model_arg = DeclareLaunchArgument(
        "model",
        default_value="framedog.urdf.xacro",
        description="Xacro file in urdf/ to load "
        "(framedog.urdf.xacro = full robot, legs_display.urdf.xacro = both legs).",
    )

    xacro_path = PathJoinSubstitution([FindPackageShare(pkg), "urdf", LaunchConfiguration("model")])
    robot_description = ParameterValue(
        Command([FindExecutable(name="xacro"), " ", xacro_path]), value_type=str
    )

    rviz_file = os.path.join(pkg_share, "rviz", "framedog.rviz")

    return LaunchDescription(
        [
            model_arg,
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[{"robot_description": robot_description}],
            ),
            Node(
                package="joint_state_publisher_gui",
                executable="joint_state_publisher_gui",
                name="joint_state_publisher_gui",
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                arguments=["--display-config", rviz_file],
            ),
        ]
    )
