cmake_minimum_required(VERSION 2.8)

project( displayImage )

find_package( OpenCV REQUIRED )

add_executable( displayImage displayCamera.cpp )

target_link_libraries( displayImage ${OpenCV_LIBS} )
