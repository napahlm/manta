cmake_minimum_required(VERSION 3.0.2)
project(manta_msgs)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  geometry_msgs
  message_generation
  std_msgs
)

add_message_files(
  DIRECTORY msg
  FILES
  Propulsion.msg
  Pwm.msg
)

generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
)

catkin_package(
# LIBRARIES manta_msgs
 CATKIN_DEPENDS
 geometry_msgs
 message_generation
 std_msgs
 message_runtime
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
