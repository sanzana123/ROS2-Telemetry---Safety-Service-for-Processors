#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# 1. Import the message type you need
# Example: from std_msgs.msg import String, Int32
# Example: from sensor_msgs.msg import Temperature, Image

class MinimalPublisher(Node):
    def __init__(self):
        # 2. Pass the node name to the superclass constructor
        super().__init__("publisher_node_name")

        # 3. Create the publisher: create_publisher(MsgType, 'topic_name', qos_profile_depth)
        # self.publisher_ = self.create_publisher(MessageType, "topic_name", 10)

        # 4. Create a timer to call the publishing callback periodically (e.g., every 1.0 second)
        timer_period = 1.0  # seconds
        self.timer_ = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info("Publisher Node has been started.")

    def timer_callback(self):
        # 5. Instantiate, populate, and publish your message
        # msg = MessageType()
        # msg.data = "Your payload here"
        # self.publisher_.publish(msg)

        # self.get_logger().info(f"Published: {msg.data}")
        pass

def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()