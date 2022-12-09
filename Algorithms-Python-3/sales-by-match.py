
import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    countOfSocks = []
    for sock in set(ar):
        countOfSocks.append(ar.count(sock))
    return sum([i//2 for i in countOfSocks])


if __name__ == '__main__':

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
