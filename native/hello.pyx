cdef extern from "hello.h":
    int add(int a, int b)

def add_numbers_from_c(int a, int b):
    return add(a, b)