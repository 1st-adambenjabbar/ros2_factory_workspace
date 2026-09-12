"""Launch the validated robot description in robot_state_publisher."""

from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    xacro_file = PathJoinSubstitution(
        [FindPackageShare("dog_robot_description"), "urdf", "dog_robot.urdf.xacro"]
    )
    robot_description = {"robot_description": Command(["xacro ", xacro_file])}

    return LaunchDescription(
        [
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                parameters=[robot_description],
                output="screen",
            ),
        ]
    )
