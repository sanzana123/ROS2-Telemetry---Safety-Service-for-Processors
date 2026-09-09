#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# 1. Import the message type matching the topic you are listening to
from std_msgs.msg import Float32 
from example_interfaces.srv import SetBool


class monitor_temperature(Node):
    def __init__(self):
        # 2. Pass the node name to the superclass constructor
        super().__init__("thermal_monitor_node")


        # 3. Create the subscriber: create_subscription(MsgType, 'topic_name', callback_fn, qos_profile_depth)
        self.subscription_ = self.create_subscription(
            Float32,
            "temperature",
            self.listener_callback,
            10
        )

        self.get_logger().info("Subscriber Node has been started.")

        self.client = self.create_client(SetBool, "reset_health_alarm")


    def send_request(self):
        # 3. Construct the request object
        request = SetBool.Request()
        request.data = True 

        # 2. Wait until the service server is online
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service server to become available...")

        
        
        # 4. Call the service asynchronously
        future = self.client.call_async(request)
        return future



    def listener_callback(self, msg):
        # 4. Process the incoming message inside the callback

        self.critical_temp = 75.0 
        if (msg.data > self.critical_temp): 
            self.get_logger().warn(f"Critical temperature Crossed: OVERHEATING Detected!")

        pass

def main(args=None):
    rclpy.init(args=args)
    client_node = monitor_temperature()

    #send request with inputs 
    future = client_node.send_request()

    try:
        rclpy.spin(client_node)
    except KeyboardInterrupt:
        pass
    finally:
        client_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()