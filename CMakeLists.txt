cmake_minimum_required(VERSION 3.0.2)
project(hello_world)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)


## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

## To declare and build messages, services or actions from within this
## package, follow these steps:
## * Let MSG_DEP_SET be the set of packages whose message types you use in
##   your messages/services/actions (e.g. std_msgs, actionlib_msgs, ...).
## * In the file package.xml:
##   * add a build_depend tag for "message_generation"
##   * add a build_depend and a exec_depend tag for each package in MSG_DEP_SET
##   * If MSG_DEP_SET isn't empty the following dependency has been pulled in
##     but can be declared for certainty nonetheless:
##     * add a exec_depend tag for "message_runtime"
## * In this file (CMakeLists.txt):
##   * add "message_generation" and every package in MSG_DEP_SET to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * add "message_runtime" and every package in MSG_DEP_SET to
##     catkin_package(CATKIN_DEPENDS ...)
##   * uncomment the add_*_files sections below as needed
##     and list every .msg/.srv/.action file to be processed
##   * uncomment the generate_messages entry below
##   * add every package in MSG_DEP_SET to generate_messages(DEPENDENCIES ...)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  IoTsensor.msg
  temp_sensor.msg
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  AddTwoInts.srv
  Area.srv
  coordinates_check.srv
  reach_goal.srv
  power_service.srv
)

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

## To declare and build dynamic reconfigure parameters within this
## package, follow these steps:
## * In the file package.xml:
##   * add a build_depend and a exec_depend tag for "dynamic_reconfigure"
## * In this file (CMakeLists.txt):
##   * add "dynamic_reconfigure" to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * uncomment the "generate_dynamic_reconfigure_options" section below
##     and list every .cfg file to be processed

## Generate dynamic reconfigure parameters in the 'cfg' folder
# generate_dynamic_reconfigure_options(
#   cfg/DynReconf1.cfg
#   cfg/DynReconf2.cfg
# )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES hello_world
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
# add_library(${PROJECT_NAME}
#   src/${PROJECT_NAME}/hello_world.cpp
# )

## Add cmake target dependencies of the library
## as an example, code may need to be generated before libraries
## either from message generation or dynamic reconfigure
# add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Declare a C++ executable
## With catkin_make all packages are built within a single CMake context
## The recommended prefix ensures that target names across packages don't collide
# add_executable(${PROJECT_NAME}_node src/hello_world_node.cpp)

## Rename C++ executable without prefix
## The above recommended prefix causes long target names, the following renames the
## target back to the shorter version for ease of user use
## e.g. "rosrun someones_pkg node" instead of "rosrun someones_pkg someones_pkg_node"
# set_target_properties(${PROJECT_NAME}_node PROPERTIES OUTPUT_NAME node PREFIX "")

## Add cmake target dependencies of the executable
## same as for the library above
# add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
# target_link_libraries(${PROJECT_NAME}_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination

##scripts
#add_service
catkin_install_python(PROGRAMS src/scripts/add_service/add_server.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/add_service/add_client.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#area_service
catkin_install_python(PROGRAMS src/scripts/area_service/area_server.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/area_service/area_client.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#coordinates_check
catkin_install_python(PROGRAMS src/scripts/coordinates_check/coordinates_check_server.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/coordinates_check/coordinates_check_client.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#data
catkin_install_python(PROGRAMS src/scripts/data/data.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/data/IMU_data_sub.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/data/IMU_data.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#IoT_sensor
catkin_install_python(PROGRAMS src/scripts/IoT_sensor/IoT_sensor_pub.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/IoT_sensor/IoT_sensor_sub.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#OOP
catkin_install_python(PROGRAMS src/scripts/OOP/oop_1.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/OOP/oop_2.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#power_service
catkin_install_python(PROGRAMS src/scripts/power_service/power_server.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/power_service/power_client.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#reach_goal_service
catkin_install_python(PROGRAMS src/scripts/reach_goal_service/reach_goal_server.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/reach_goal_service/reach_goal_client.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#some_sensor
catkin_install_python(PROGRAMS src/scripts/some_sensor/some_sensor_pub.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/some_sensor/some_sensor_sub.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#talker_listner
catkin_install_python(PROGRAMS src/scripts/talker_listner/talker.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/talker_listner/listner.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#temp_sensor
catkin_install_python(PROGRAMS src/scripts/temp_sensor/temp_sensor_pub.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/scripts/temp_sensor/temp_sensor_sub.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#test
catkin_install_python(PROGRAMS src/scripts/test/test.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#turtle_motion
catkin_install_python(PROGRAMS src/scripts/turtle_motion/motion_cleaner.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})


##perception
#camera
catkin_install_python(PROGRAMS src/perception/camera/camera.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#color_filtering
catkin_install_python(PROGRAMS src/perception/color_filtering/color_filtering.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#copy

#CVBridge
catkin_install_python(PROGRAMS src/perception/CVBridge/CVBridge.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#edge_detection
catkin_install_python(PROGRAMS src/perception/edge_detection/edge_detection.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#img_encoding
catkin_install_python(PROGRAMS src/perception/img_encoding/img_encoding.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#img_structure
catkin_install_python(PROGRAMS src/perception/img_structure/img_structure.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#open_copy
catkin_install_python(PROGRAMS src/perception/open_copy/open_copy.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#squash_ball_detection
catkin_install_python(PROGRAMS src/perception/squash_ball_detection/squash_ball_detection.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS src/perception/squash_ball_detection/squash_ball_camera.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#thresholding
catkin_install_python(PROGRAMS src/perception/thresholding/thresholding.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})


## Mark executables for installation
## See http://docs.ros.org/melodic/api/catkin/html/howto/format1/building_executables.html
# install(TARGETS ${PROJECT_NAME}_node
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark libraries for installation
## See http://docs.ros.org/melodic/api/catkin/html/howto/format1/building_libraries.html
# install(TARGETS ${PROJECT_NAME}
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
# )

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )
#reach_goal_service for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_hello_world.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
