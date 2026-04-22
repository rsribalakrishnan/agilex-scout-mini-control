# AgileX Scout Mini Remote Control using Xbox Controller and Jetson Xavier NX

## Overview
This project focuses on enabling remote control of the AgileX Scout Mini robotic platform using an Xbox controller. The system bridges communication between the joystick and the Scout Mini through an NVIDIA Jetson Xavier NX, with ROS nodes managing communication and command flow.

The core objective of the project was to establish end-to-end control from the Xbox controller to the AgileX platform, including hardware setup, CAN communication, ROS node deployment, and auto-boot execution on the Jetson board. At the current stage documented in this project, the platform supports linear motion control. :contentReference[oaicite:2]{index=2}

## Project Goals
- Connect the AgileX Scout Mini with an Xbox controller
- Use the NVIDIA Jetson Xavier NX as the intermediate compute unit
- Enable communication between the controller and the robot through ROS-based nodes
- Configure CAN communication between Jetson and Scout Mini
- Automate script execution on system boot
- Achieve reliable motion control of the robot platform

## System Architecture
The system consists of the following major components:
- **AgileX Scout Mini platform**
- **NVIDIA Jetson Xavier NX**
- **Xbox controller**
- **CAN adapter**
- **ROS nodes for joystick and robot command handling**
- **Boot-time shell scripts for automated startup**

In this setup, the Xbox controller sends user inputs to the Jetson Xavier NX, which processes these commands and forwards motion instructions to the AgileX Scout Mini over the CAN interface. :contentReference[oaicite:3]{index=3}

## Features
- Xbox-controller-based remote operation
- CAN-based communication between Jetson and Scout Mini
- ROS node-based modular communication
- Auto-boot script execution on startup
- Experimental testing and debugging of joystick-to-robot command flow
- Linear motion control demonstration

## Hardware Used
- AgileX Scout Mini
- NVIDIA Jetson Xavier NX
- CAN adapter provided with the Scout Mini
- Xbox controller
- External power converter
- Wiring and mounting accessories for board integration

The uploaded project notes also describe work on mounting the Jetson board onto the Scout Mini and supplying power correctly through the voltage converter. :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

## Software Stack
- Ubuntu on Jetson Xavier NX
- ROS Noetic
- Python
- Shell scripts
- SocketCAN / CAN utilities
- pygame for controller-side experimentation
- pyagxrobots repository / AgileX-related Python integration tools

The project notes explicitly mention ROS Noetic, Python scripts, shell scripts, CAN utilities, and testing with pygame for Xbox controller input. :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7}


│   └── weekly_updates.md
└── assets/
    └── architecture_diagram.png
