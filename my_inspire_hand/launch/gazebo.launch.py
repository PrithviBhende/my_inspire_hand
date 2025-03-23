import os
import launch
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, RegisterEventHandler
from launch_ros.actions import Node
from launch.event_handlers import OnProcessStart

def generate_launch_description():
    pkg_path = get_package_share_directory('my_inspire_hand')
    
    return LaunchDescription([
        # Start Gazebo first
        ExecuteProcess(
            cmd=['gz', 'sim', '-v', '4', '-r', 'empty.sdf'],
            output='screen'
        ),
        
        # Add 5-second delay before spawning
        RegisterEventHandler(
            event_handler=OnProcessStart(
                target_action=launch.actions.LogInfo(msg='Starting spawn process'),
                on_start=[
                    Node(
                        package='ros_gz_sim',
                        executable='create',
                        arguments=[
                            '-file', os.path.join(pkg_path, 'urdf', 'inspire_hand_left.urdf'),
                            '-name', 'inspire_hand',
                            '-z', '0.5',
                            '-world', 'default'
                        ],
                        output='screen'
                    )
                ]
            )
        )
    ])
