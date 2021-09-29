cmake_minimum_required(VERSION 3.5)
project(decoder_lib)

# Extra lib files for WIN32
if(WIN32)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()

# Create a library
add_library(decoder_lib SHARED decoder.c)
target_include_directories(decoder_lib PUBLIC ${PROJECT_SOURCE_DIR})

# Create an executable
# add_executable(print_os_name src/main.c)
# target_link_libraries(print_os_name PRIVATE get_os_library)