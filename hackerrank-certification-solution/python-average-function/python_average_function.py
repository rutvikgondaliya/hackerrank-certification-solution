
import math
import os
import random
import re
import sys


# write your code here

def avg(*num):
    if num == 0:
        return None
    sum = 0
    for i in num:
        sum = sum + i
        total = sum / len(num)
    return total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
