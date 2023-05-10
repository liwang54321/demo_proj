cmake_minimum_required(VERSION 3.0.0)
project(test_place VERSION 0.1.0)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 20)

include(ProcessorCount)
ProcessorCount(N)
message("number of processors: "  ${N})
if(NOT N EQUAL 0)
  set(CTEST_BUILD_FLAGS -j${N})
  set(ctest_test_args ${ctest_test_args} PARALLEL_LEVEL ${N})
  set(CMAKE_MAKE_PROGRAM "${CMAKE_MAKE_PROGRAM} -j ${N}")      
endif()
message("cmake make program" ${CMAKE_MAKE_PROGRAM})

# execute_process(COMMAND 
#     conan install 
#     ${CMAKE_CURRENT_SOURCE_DIR}/conanfile.py 
#     --build=missing 
#     -pr=default 
#     -of=${CMAKE_CURRENT_BINARY_DIR}
# )

# set(CMAKE_PREFIX_PATH "${CMAKE_PREFIX_PATH} ${CMAKE_CURRENT_BINARY_DIR}")
# include(${CMAKE_CURRENT_BINARY_DIR}/conan_toolchain.cmake)

find_package(spdlog REQUIRED)
find_package(imgui REQUIRED)
find_package(asio REQUIRED)
find_package(clipp REQUIRED)
find_package(rttr REQUIRED)
find_package(Boost REQUIRED)

include(CTest)
enable_testing()

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME} spdlog::spdlog imgui::imgui asio::asio clipp::clipp RTTR::Core_Lib Boost::boost)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
