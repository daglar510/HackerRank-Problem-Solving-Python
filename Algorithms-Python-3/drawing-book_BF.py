import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n ,p):
    # Write your code here
    count1, count2 = 0, 0
    page = 1
    while page < p :
        count1 += 1
        page += 2
    page = n
    if n%2 == 1 :
        page -= 1
    while page > p :
        count2 += 1
        page -=2
    print(count1, count2)
    return min([count1, count2])


if __name__ == '__main__':

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
