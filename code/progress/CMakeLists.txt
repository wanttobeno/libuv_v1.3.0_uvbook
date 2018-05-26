############ Gen By Python Script ############

project(progress)
add_executable (${PROJECT_NAME} main.c )

############ Gen By Python Script ############

cmake_minimum_required(VERSION 2.8)

# include
include_directories( ${CMAKE_CURRENT_LIST_DIR}/../../libuv/include)

# MT MTd
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} /MTd")
set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} /MT")

set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MTd")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")

if (MSVC)
    set(CompilerFlags
        CMAKE_CXX_FLAGS
        CMAKE_CXX_FLAGS_DEBUG
        CMAKE_CXX_FLAGS_RELEASE
        CMAKE_C_FLAGS
        CMAKE_C_FLAGS_DEBUG
        CMAKE_C_FLAGS_RELEASE
        )
    foreach(CompilerFlag ${CompilerFlags})
        string(REPLACE "/MD" "/MT" ${CompilerFlag} "${${CompilerFlag}}")
    endforeach()
endif(MSVC)


# link lib
target_link_libraries(${PROJECT_NAME}
  ws2_32.lib
  psapi.lib
  iphlpapi.lib
  # debug lib
  debug  ${CMAKE_CURRENT_LIST_DIR}/../../libuv/Debug/lib/libuv.lib
  # release lib
  optimized   ${CMAKE_CURRENT_LIST_DIR}/../../libuv/Release/lib/libuv.lib
)




