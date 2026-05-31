cmake_minimum_required(VERSION 3.8)
project(dexterous_hand_core)

# Find ROS 2 build tools
find_package(ament_cmake REQUIRED)

# Install Python scripts as executable programs (no .py extensions)
install(PROGRAMS
  scripts/camera_driver_node
  scripts/teleop_input_node
  scripts/main_planning_node
  scripts/hand_actuator_node
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files to the share directory
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
