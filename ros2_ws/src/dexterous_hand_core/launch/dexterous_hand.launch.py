from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='dexterous_hand_core',
            executable='camera_driver_node',
            name='camera_driver_node',
            output='screen'
        ),
        Node(
            package='dexterous_hand_core',
            executable='main_planning_node',
            name='main_planning_node',
            output='screen'
        ),
        Node(
            package='dexterous_hand_core',
            executable='hand_actuator_node',
            name='hand_actuator_node',
            output='screen'
        )
    ])
