import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    description_pkg = get_package_share_directory("dog_robot_description")
    environment_pkg = get_package_share_directory("dog_factory_environment")
    urdf_path = os.path.join(description_pkg, "urdf", "dog.urdf.xacro")
    world_path = os.path.join(environment_pkg, "worlds", "factory.world")

    gazebo = ExecuteProcess(
        cmd=["gazebo", "--verbose", world_path, "-s", "libgazebo_ros_factory.so"],
        output="screen",
    )
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": open(urdf_path).read()}],
    )
    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description", "-entity", "dog_robot"],
        output="screen",
    )

    return LaunchDescription([gazebo, robot_state_publisher, spawn_robot])
