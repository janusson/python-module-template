#!/usr/bin/python
# -*- coding: utf-8 -*-
#   << module name >>
#   Eric Janusson
#   Python 3.9

import os
import sys
# EX: import module as mod
# x = mod.function_in_module()

# constants
filename = sys.argv[0]

# logging
import logging

# constants
start_time = time.time()
# default location of Driftscope Apex3D64.exe and logfile
apexPath = r'C:\DriftScope\lib\Apex3D64.exe'
apexLogPath = r'C:\DriftScope\log\_Apex3DLog.txt'

# logging setup # TODO
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(log_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# functions
def funk():
    print(filename)
    print(os.getcwd())
    return None

# main
def main():
    funk()

if __name__ == '__main__':
    main()
