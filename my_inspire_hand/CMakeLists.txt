cmake_minimum_required(VERSION 3.8)
project(my_inspire_hand)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

# Install directories
install(
  DIRECTORY launch urdf config
  DESTINATION share/${PROJECT_NAME}
)

# Install meshes with preserved structure
install(
  DIRECTORY urdf/meshes
  DESTINATION share/${PROJECT_NAME}/urdf
)
# Install Python scripts
install(
  PROGRAMS src/make_fist.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install config files
install(
  DIRECTORY config
  DESTINATION share/${PROJECT_NAME}
)


ament_package()
