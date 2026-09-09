#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts  # Change to your service type

class ServiceClientTemplate(Node):
    def __init__(self):
        super().__init__("service_client_node_name")
        
        # 1. Create the service client
        # Syntax: create_client(SrvType, "service_name")
        self.client = self.create_client(AddTwoInts, "service_name")
        
        # 2. Wait until the service server is online
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service server to become available...")

    def send_request(self, val_a, val_b):
        # 3. Construct the request object
        request = AddTwoInts.Request()
        request.a = val_a
        request.b = val_b
        
        # 4. Call the service asynchronously
        future = self.client.call_async(request)
        return future

def main(args=None):
    rclpy.init(args=args)
    client_node = ServiceClientTemplate()
    
    # 5. Send request with inputs
    future = client_node.send_request(10, 20)
    
    # 6. Block until the response is received from the server
    rclpy.spin_until_future_complete(client_node, future)
    
    if future.result() is not None:
        response = future.result()
        client_node.get_logger().info(f"Service call successful! Result: {response.sum}")
    else:
        client_node.get_logger().error("Service call failed.")
        
    client_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()