#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# 1. Import the message type you need
from std_msgs.msg import Float32, Int32
# Example: from sensor_msgs.msg import Temperature, Image

class MinimalPublisher(Node):
    def __init__(self):
        # 2. Pass the node name to the superclass constructor
        super().__init__("thermal_sensor_node")
        self.current_temp = 20.0 

        # 3. Create the publisher: create_publisher(MsgType, 'topic_name', qos_profile_depth)
        self.publisher_ = self.create_publisher(Float32, "temperature", 10)

        # 4. Create a timer to call the publishing callback periodically (e.g., every 1.0 second)
        timer_period = 1.0  # seconds
        self.timer_ = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info("Publisher Node has been started.")

    def timer_callback(self):
        # 5. Instantiate, populate, and publish your message
        msg = Float32()

        msg.data = self.current_temp 
        # self.publisher_.publish(msg)

        # self.get_logger().info(f"Published: {msg.data}"

        self.publisher_.publish(msg)

        self.current_temp = self.current_temp + 10

        if self.current_temp > 85.0:
            self.current_temp = 20.0 
        self.get_logger().info(f"Published: {msg.data}")

        
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