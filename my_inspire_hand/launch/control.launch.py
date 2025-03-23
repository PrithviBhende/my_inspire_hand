from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    pkg_path = get_package_share_directory('my_inspire_hand')
    controllers_path = os.path.join(pkg_path, 'config', 'controllers.yaml')
    
    return LaunchDescription([
        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[
                {'robot_description': '<robot>...</robot>'},  # Your URDF content
                controllers_path
            ]
        ),
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['joint_state_broadcaster'],
            parameters=[{'use_sim_time': True}]
        ),
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['hand_controller'],
            parameters=[{'use_sim_time': True}]
        )
    ])
