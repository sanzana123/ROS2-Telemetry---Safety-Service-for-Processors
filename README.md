# 🌡️ ROS 2 Telemetry & Safety Service for Processors

[![ROS 2](https://img.shields.io/badge/ROS%202-Jazzy%20%2F%20Humble-blue?logo=ros)](https://docs.ros.org/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A lightweight, distributed system built with ROS 2 (`rclpy`) for real-time hardware thermal monitoring and state-based alarm resets.

---

## 📌 Overview

This package demonstrates decoupling hardware telemetry, critical threshold checks, and system safety services across independent ROS 2 nodes.

### 🧩 Architecture at a Glance

[ Thermal Sensor Node ]
             │
             │  Published Topic: /temperature (std_msgs/Float32)
             ▼
[ Thermal Monitor Node ]
             │
             │  Service Client: /reset_health_alarm (example_interfaces/SetBool)
             ▼
[ Health Service Node ]

## ⚙️ Node Breakdown

| Node Name | Role | Interface / Topic | Description |
| :--- | :--- | :--- | :--- |
| **`thermal_sensor_node`** | Publisher | `/temperature` <br>`(std_msgs/msg/Float32)` | Simulates thermal telemetry, incrementing temperature readings from $20.0^\circ\text{C}$ to $85.0^\circ\text{C}$. |
| **`thermal_monitor_node`** | Subscriber / Service Client | `/reset_health_alarm` <br>`(example_interfaces/srv/SetBool)` | Monitors telemetry for overheating ($>75.0^\circ\text{C}$) and calls the health reset service. |
| **`health_service_node`** | Service Server | `/reset_health_alarm` | Tracks overall system alarm state and processes health reset requests. |

---

## 🚀 Quick Start

### 1. Prerequisities & Environment
* **OS**: Ubuntu 22.04 / 24.04 (or Linux container)
* **ROS 2**: Jazzy, Humble, or Iron
* **Build Tool**: `colcon`

### 2. Build the Package

# Navigate to your workspace root
cd ~/ros2_ws

# Build the package with symlink install for rapid iteration
colcon build --packages-select my_py_pkg --symlink-install

# Source the workspace setup script
source install/setup.bash 

# Run nodes in 3 different terminals 
* ros2 run my_py_pkg health_service_node
* ros2 run my_py_pkg thermal_monitor_node
* ros2 run my_py_pkg health_service_node


