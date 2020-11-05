#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    n = len(arr)
    max_sum = -100
    for i in range(n - 2):
        for j in range(n - 2):
            _sum = arr[i + 1][j + 1]
            for i2 in range(i, i + 3, 2):
                for j2 in range(j, j + 3):
                    _sum += arr[i2][j2] 
                    
            if max_sum < _sum:
                max_sum = _sum
    print(max_sum)
