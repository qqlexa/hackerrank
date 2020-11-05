#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    
    binary_number = ""
    while n != 0:
        if n % 2:
            binary_number += "1"
            n -= 1
        else:
            binary_number += "0"    
        n /= 2
        
    binary_number = binary_number[::-1]

    max_line = 0
    cur_line = 0
    for i in binary_number:
        if i == "1":
            cur_line += 1
        else:
            if cur_line > max_line:
                max_line = cur_line
            cur_line = 0
    if cur_line > max_line:
        max_line = cur_line
    print(max_line)
