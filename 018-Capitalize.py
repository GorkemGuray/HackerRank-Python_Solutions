#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    list1 = s.split(" ")
    list2 = []

    for i in list1:
        list2.append(i.capitalize())

    sss = ' '.join(list2)
    return sss 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
