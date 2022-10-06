# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "challenge_one: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ichallenge_one:/root/catkin_ws/src/challenge_one/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(challenge_one_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/root/catkin_ws/src/challenge_one/msg/Completed.msg" NAME_WE)
add_custom_target(_challenge_one_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "challenge_one" "/root/catkin_ws/src/challenge_one/msg/Completed.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(challenge_one
  "/root/catkin_ws/src/challenge_one/msg/Completed.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/challenge_one
)

### Generating Services

### Generating Module File
_generate_module_cpp(challenge_one
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/challenge_one
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(challenge_one_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(challenge_one_generate_messages challenge_one_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/catkin_ws/src/challenge_one/msg/Completed.msg" NAME_WE)
add_dependencies(challenge_one_generate_messages_cpp _challenge_one_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(challenge_one_gencpp)
add_dependencies(challenge_one_gencpp challenge_one_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS challenge_one_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(challenge_one
  "/root/catkin_ws/src/challenge_one/msg/Completed.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/challenge_one
)

### Generating Services

### Generating Module File
_generate_module_eus(challenge_one
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/challenge_one
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(challenge_one_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(challenge_one_generate_messages challenge_one_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/catkin_ws/src/challenge_one/msg/Completed.msg" NAME_WE)
add_dependencies(challenge_one_generate_messages_eus _challenge_one_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(challenge_one_geneus)
add_dependencies(challenge_one_geneus challenge_one_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS challenge_one_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(challenge_one
  "/root/catkin_ws/src/challenge_one/msg/Completed.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/challenge_one
)

### Generating Services

### Generating Module File
_generate_module_lisp(challenge_one
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/challenge_one
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(challenge_one_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(challenge_one_generate_messages challenge_one_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/catkin_ws/src/challenge_one/msg/Completed.msg" NAME_WE)
add_dependencies(challenge_one_generate_messages_lisp _challenge_one_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(challenge_one_genlisp)
add_dependencies(challenge_one_genlisp challenge_one_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS challenge_one_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(challenge_one
  "/root/catkin_ws/src/challenge_one/msg/Completed.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/challenge_one
)

### Generating Services

### Generating Module File
_generate_module_nodejs(challenge_one
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/challenge_one
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(challenge_one_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(challenge_one_generate_messages challenge_one_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/catkin_ws/src/challenge_one/msg/Completed.msg" NAME_WE)
add_dependencies(challenge_one_generate_messages_nodejs _challenge_one_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(challenge_one_gennodejs)
add_dependencies(challenge_one_gennodejs challenge_one_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS challenge_one_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(challenge_one
  "/root/catkin_ws/src/challenge_one/msg/Completed.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/challenge_one
)

### Generating Services

### Generating Module File
_generate_module_py(challenge_one
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/challenge_one
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(challenge_one_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(challenge_one_generate_messages challenge_one_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/catkin_ws/src/challenge_one/msg/Completed.msg" NAME_WE)
add_dependencies(challenge_one_generate_messages_py _challenge_one_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(challenge_one_genpy)
add_dependencies(challenge_one_genpy challenge_one_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS challenge_one_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/challenge_one)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/challenge_one
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(challenge_one_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(challenge_one_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/challenge_one)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/challenge_one
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(challenge_one_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(challenge_one_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/challenge_one)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/challenge_one
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(challenge_one_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(challenge_one_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/challenge_one)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/challenge_one
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(challenge_one_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(challenge_one_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/challenge_one)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/challenge_one\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/challenge_one
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(challenge_one_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(challenge_one_generate_messages_py geometry_msgs_generate_messages_py)
endif()
