cmake_minimum_required(VERSION 3.16)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

EXECUTE_PROCESS( COMMAND uname -m COMMAND tr -d '\n' OUTPUT_VARIABLE ARCHITECTURE )
message( STATUS "Architecture: ${ARCHITECTURE}" )

if(${ARCHITECTURE} STREQUAL "x86_64")
    SET (CMAKE_C_COMPILER         "/usr/bin/clang-12")
else()
    SET (CMAKE_C_COMPILER         "/usr/bin/gcc-10")
endif()
SET (CMAKE_C_FLAGS                "-Wall -std=c99")
SET (CMAKE_C_FLAGS_DEBUG          "-g")
SET (CMAKE_C_FLAGS_MINSIZEREL     "-Os -DNDEBUG")
SET (CMAKE_C_FLAGS_RELEASE        "-O3 -DNDEBUG")
SET (CMAKE_C_FLAGS_RELWITHDEBINFO "-O2 -g")

if(${ARCHITECTURE} STREQUAL "x86_64")
    SET (CMAKE_CXX_COMPILER         "/usr/bin/clang++-12")
else()
    SET (CMAKE_CXX_COMPILER         "/usr/bin/g++-10")
endif()
SET (CMAKE_CXX_FLAGS                "-Wall -pedantic")
SET (CMAKE_CXX_FLAGS_DEBUG          "-g")
SET (CMAKE_CXX_FLAGS_MINSIZEREL     "-Os -DNDEBUG -fno-exceptions")
SET (CMAKE_CXX_FLAGS_RELEASE        "-O3 -DNDEBUG -fno-exceptions")
SET (CMAKE_CXX_FLAGS_RELWITHDEBINFO "-O2 -g")

SET (CMAKE_AR      "/usr/bin/llvm-ar")
SET (CMAKE_LINKER  "/usr/bin/llvm-ld")
SET (CMAKE_NM      "/usr/bin/llvm-nm")
SET (CMAKE_OBJDUMP "/usr/bin/llvm-objdump")
SET (CMAKE_RANLIB  "/usr/bin/llvm-ranlib")

get_filename_component(RootFolderName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
project(${RootFolderName} VERSION 1.0)

set(BUILD_SHARED_LIBS OFF)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

add_subdirectory(src)