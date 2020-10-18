# https://www.hackerrank.com/challenges/mini-max-sum
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0
    for j in range(1, len(arr)):
        min_sum += arr[j]
        max_sum += arr[j]

    sum_result = 0
    for i in range(len(arr)):
        sum_result = 0
        for j in range(len(arr)):
            if i != j:
                sum_result += arr[j]
        if min_sum > sum_result:
            min_sum = sum_result
        elif max_sum < sum_result:
            max_sum = sum_result
    print(min_sum, end=" ")
    print(max_sum)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
