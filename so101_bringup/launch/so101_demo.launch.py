from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import TimerAction
import os


def generate_launch_description():
    so101_moveit_dir = os.path.join(
        get_package_share_directory("so101_moveit_description")
    )

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(so101_moveit_dir, "launch", "demo.launch.py")
            )
        ),
        TimerAction(
            period=2.0,
            actions=[
                Node(
                    package="so101_driver",
                    executable="so101_joint_trajectory_controller",
                    name="so101_joint_trajectory_controller",
                    output="screen",
                )
            ],
        ),
    ])
