cmake_minimum_required(VERSION 3.0.2)
project(dexterous_hand_core)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  geometry_msgs
  std_msgs
  cv_bridge
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES dexterous_hand_core
#  CATKIN_DEPENDS rospy sensor_msgs geometry_msgs std_msgs cv_bridge
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/camera_driver_node.py
  scripts/teleop_input_node.py
  scripts/main_planning_node.py
  scripts/hand_actuator_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
