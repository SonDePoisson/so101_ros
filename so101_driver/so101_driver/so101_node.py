import rclpy
from rclpy.node import Node
from .so101_driver import SO101Driver

RATE = 20  # Hz


class SO101DriverNode(Node):
    def __init__(self):
        super().__init__("so101_driver_node")
        self.driver = SO101Driver()

        if self.driver.detect():
            self.get_logger().error("Detection Failed : Empty motor list")

        self.create_timer(1 / RATE, self.update)

    def update(self):
        pass


def main(args=None):
    rclpy.init(args=args)
    node = SO101DriverNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
