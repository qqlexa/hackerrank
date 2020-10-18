# https://www.hackerrank.com/challenges/picking-numbers
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    for j in range(len(a)):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

    currently_len = 1;
    currently_min = a[0]
    max_len = 1;
    
    for i in range(1, len(a)):
        difference = a[i] - currently_min
        if difference > 1:
            if currently_len > max_len:
                max_len = currently_len
            currently_min = a[i]
            currently_len = 1
        else:
            currently_len += 1
    if currently_len > max_len:
        max_len = currently_len
    return max_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
