#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts  # Change to your service type

class ServiceServerTemplate(Node):
    def __init__(self):
        super().__init__("service_server_node_name")
        
        # 1. Create the service server
        # Syntax: create_service(SrvType, "service_name", callback_function)
        self.srv = self.create_service(
            AddTwoInts, 
            "service_name", 
            self.service_callback
        )
        self.get_logger().info("Service Server template started.")

    def service_callback(self, request, response):
        # 2. Process the request inputs and assign values to response fields
        response.sum = request.a + request.b
        
        self.get_logger().info(f"Incoming request: a={request.a}, b={request.b}")
        self.get_logger().info(f"Sending back response: sum={response.sum}")
        
        # 3. Always return the response object
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ServiceServerTemplate()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()