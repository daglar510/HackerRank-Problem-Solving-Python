import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    maxA = max(a)
    minB = min(b)
    count = 0
    for num in range(maxA, minB + 1):
        left = all([num % numA == 0 for numA in a])
        right = all([numB % num == 0 for numB in b])
        count += left * right
    return count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #one in the top is what Hackerrank uses but we do not need the file pointer to open this way we want it to just go to standard output
    fptr = sys.stdout   # stdout is already an open stream
#     Note that on the one hand, os.environ['OUTPUT_PATH'] is a string, while fptr is a stream/file pointer.
#
#Variations:

#If you want to write to a file, you can do it the way suggested above (setting the OUTPUT_PATH environment variable).
#
#Or, you can set the os.environ directly in python, e.g.
#
#os.environ['OUTPUT_PATH'] = 'junk.txt'  # before you open the fptr!
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')
