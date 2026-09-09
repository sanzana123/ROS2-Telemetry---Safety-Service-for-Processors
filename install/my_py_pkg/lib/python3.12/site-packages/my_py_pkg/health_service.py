#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool

class ServiceServerTemplate(Node):
    def __init__(self):
        super().__init__("health_service_node")

        self.alarm_active = True
        
        # 1. Create the service server
        # Syntax: create_service(SrvType, "service_name", callback_function)
        self.srv = self.create_service(
            SetBool, 
            "reset_health_alarm", 
            self.service_callback
        )
        self.get_logger().info("Service Server template started.")

    def service_callback(self, request, response):
        # 2. Process the request inputs and assign values to response fields
        

        if (request.data == True):
            self.alarm_active = False
            response.success = True 
            response.message = "System alarm successfully cleared"
        else:
            response.success = False 
            response.message = "System alarm has not been successfully cleared"
        
        self.get_logger().info(f"Incoming request: {request.data}")
        self.get_logger().info(f"Sending back response: Success={response.success}")
        
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