## 📌 Overview

**ROS 2 Telemetry Safety Service for Processors** is a distributed, multi-node software package developed in Python (`rclpy`) for real-time system safety monitoring and automated health management. 

The architecture decouples telemetry generation, state monitoring, and system resets across three independent ROS 2 nodes communicating via Data Distribution Service (DDS) middleware primitives:

- **Thermal Sensor Node (`thermal_sensor_node`)**: Simulates continuous thermal hardware telemetry by streaming floating-point temperature data to the `/temperature` topic (`std_msgs/msg/Float32`).
- **Thermal Monitor Node (`thermal_monitor_node`)**: Subscribes to the thermal stream, evaluates data against a critical safety threshold ($75.0^\circ\text{C}$), and triggers asynchronous service dispatches upon anomaly detection.
- **Health Service Node (`health_service_node`)**: Maintains persistent system state and hosts the `/reset_health_alarm` service server (`example_interfaces/srv/SetBool`) to process alarm clear requests.

---

### 🎯 Key Engineering Highlights

- **Decoupled Architecture**: Independent process execution with zero shared memory, ready for multi-machine deployment over DDS.
- **Asynchronous Service Communication**: Non-blocking service client verification ensuring node responsiveness during health state resets.
- **Robust Development Workflow**: Configured with `colcon` entry points and `--symlink-install` for rapid iteration and deployment.
