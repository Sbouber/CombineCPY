#!/usr/bin/env python

import ctypes
from threading import Thread

LIB = './cpy.so'

def main():

    # Load the library
    cpy = ctypes.CDLL(LIB)

    # arg types
    cpy.some_function.argtypes = [ctypes.c_int]

    # return types
    cpy.some_function.restype = ctypes.c_int
    cpy.endless_loop.restype = ctypes.c_int

    device_id = ctypes.c_int(11)

    # Call some_function
    ret = cpy.some_function(device_id)

    print "some_function returned %s" % (ret)

    print "now trying the endless loop in thread..."
    t = Thread(target=cpy.endless_loop)
    t.start()
    print "return from endless loop"




if __name__ == '__main__':
    main()


