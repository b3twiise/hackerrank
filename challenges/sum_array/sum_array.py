# Given an array of integers, find the sum of its elements.

# For example, if the array
# , , so return

# .

# Function Description

# Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

# simpleArraySum has the following parameter(s):

#     ar: an array of integers

# Input Format

# The first line contains an integer,
# , denoting the size of the array.
# The second line contains

# space-separated integers representing the array's elements.

# Constraints

# Output Format

# Print the sum of the array's elements as a single integer.

# Sample Input

# 6
# 1 2 3 4 10 11

# Sample Output

# 31



#!/bin/python3
import sys
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setup import *


os.environ['OUTPUT_PATH'] = "sum_array.out"
os.environ['INPUT_PATH'] = "sum_array.in"

setWorkSpace()
print(os.environ['INPUT_PATH'])

from functools import reduce
def simpleArraySum(ar):
	
	return reduce(lambda x,y : x+y, ar)

	
with open(os.environ['INPUT_PATH'], 'r') as i_ptr: 
	with open(os.environ['OUTPUT_PATH'], 'w') as o_ptr: 
		ar_count = i_ptr.readline()
		ar = list(map(int, i_ptr.readline().split()))
		result  = simpleArraySum(ar)
		o_ptr.write(str(result))
		o_ptr.write("\n")
	o_ptr.close()
i_ptr.close()

