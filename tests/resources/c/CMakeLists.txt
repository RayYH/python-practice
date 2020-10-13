cmake_minimum_required(VERSION 3.16)
project(add C)
set(CMAKE_C_STANDARD 11)

set(mylibSRCS add.c)

add_library(${PROJECT_NAME} SHARED ${mylibSRCS})

set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME "add")
set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".so")
