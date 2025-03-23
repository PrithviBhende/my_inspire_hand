import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class HandController(Node):
    def __init__(self):
        super().__init__('hand_controller')
        self.joint_names = [
            'thumb_proximal_yaw_joint',
            'thumb_proximal_pitch_joint',
            'index_proximal_joint',
            'middle_proximal_joint',
            'ring_proximal_joint',
            'pinky_proximal_joint'
        ]
        
        self.publisher = self.create_publisher(
            JointTrajectory,
            '/hand_controller/joint_trajectory',
            10
        )
        
        self.timer = self.create_timer(1.0, self.send_command)
        
    def send_command(self):
        trajectory_msg = JointTrajectory()
        trajectory_msg.joint_names = self.joint_names
        
        point = JointTrajectoryPoint()
        point.positions = [0.0, 1.57, 1.57, 1.57, 1.57, 1.57]  # Fist positions
        point.time_from_start = Duration(sec=2, nanosec=0)
        
        trajectory_msg.points.append(point)
        self.publisher.publish(trajectory_msg)
        self.get_logger().info('Command sent')

def main(args=None):
    rclpy.init(args=args)
    controller = HandController()
    try:
        rclpy.spin(controller)
    except KeyboardInterrupt:
        pass
    finally:
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
