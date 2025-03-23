from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[
                {'robot_description': '<robot>...</robot>'},  # Your URDF content
                '$(find my_inspire_hand)/config/controllers.yaml'
            ]
        ),
        Node(
            package='controller_manager',
            executable='spawner.py',
            arguments=['joint_state_broadcaster']
        ),
        Node(
            package='controller_manager',
            executable='spawner.py',
            arguments=['hand_controller']
        )
    ])
