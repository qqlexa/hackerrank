# https://www.hackerrank.com/challenges/extra-long-factorials/problem
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    print(result)


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)

