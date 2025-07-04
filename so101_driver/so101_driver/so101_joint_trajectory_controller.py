import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from .so101_driver import SO101Driver

JOINT_NAMES = [
    "Shoulder_Rotation",
    "Shoulder_Pitch",
    "Elbow",
    "Wrist_Pitch",
    "Wrist_Roll",
    "Gripper",
]


class SO101JointTrajectoryController(Node):
    def __init__(self):
        super().__init__("so101_joint_trajectory_controller")
        self.driver = SO101Driver()
        self.joint_state_pub = self.create_publisher(JointState, "joint_states", 10)
        self.create_subscription(
            JointTrajectory,
            "so101_arm_controller/joint_trajectory",
            self.trajectory_callback,
            10,
        )
        self.timer = self.create_timer(0.05, self.publish_joint_states)

    def trajectory_callback(self, msg: JointTrajectory):
        for point in msg.points:
            for name, pos in zip(msg.joint_names, point.positions):
                self.driver.write_motor_pos(name, pos)

    def publish_joint_states(self):
        js = JointState()
        js.header = Header()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = JOINT_NAMES
        js.position = [self.driver.read_motor_pos(j) for j in JOINT_NAMES]
        self.joint_state_pub.publish(js)


def main(args=None):
    rclpy.init(args=args)
    node = SO101JointTrajectoryController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
