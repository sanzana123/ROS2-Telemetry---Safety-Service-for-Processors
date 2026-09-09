#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# 1. Import the message type matching the topic you are listening to
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        # 2. Pass the node name to the superclass constructor
        super().__init__("subscriber_node_name")

        # 3. Create the subscriber: create_subscription(MsgType, 'topic_name', callback_fn, qos_profile_depth)
        self.subscription_ = self.create_subscription(
            String,
            "topic_name",
            self.listener_callback,
            10
        )

        self.get_logger().info("Subscriber Node has been started.")

    def listener_callback(self, msg):
        # 4. Process the incoming message inside the callback
        self.get_logger().info(f"Received message: {msg.data}")
        pass

def main(args=None):
    rclpy.init(args=args)
    node = MinimalSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()