cmake_minimum_required(VERSION 3.4)

# Project Name
project(HelloLibrary)

# Generate shared / static librarry for hello.c
# STATIC generates `libhello.a`
# SHARED geneartes `libhello.so`
add_library(hello STATIC hello.c)