#https://www.hackerrank.com/challenges/diagonal-difference
import sys

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setup import *

os.environ["INPUT_PATH"] = "diagonal_difference.in"
os.environ["OUTPUT_PATH"] = "diagonal_difference.out"
os.environ["EXP_PATH"] = "diagonal_difference.exp"


setWorkSpace()
from functools import reduce
def diagonalDifference(matrick):
	# 0 1 2

	# 1 2 3
	# 4 5 6
	# 9 8 9  

	left_right = 0 
	right_left = 0

	#We are promised a squared matrix so here we use len(arr[0])
	n = len(matrick[0])
	close_in = n - 1
	for i in range(n):
		left_right += matrick[i][i]

		right_left += matrick[i][close_in - i]
	return abs(left_right - right_left)


my_arr = [
	[1,2,3],
	[4,5,6],
	[9,8,9]
]

with open(os.environ['INPUT_PATH'], 'r') as read_h:
	my_in = []
	c = int(read_h.readline())
	while c > 0:
		get_l_in = list(map(int, read_h.readline().split()))
		my_in.append(get_l_in)
		c -= 1
	read_h.close()
print(my_in)

with open(os.environ['OUTPUT_PATH'], 'w') as write_h:
	my_out = diagonalDifference(my_in)
	write_h.write(str(my_out))
	write_h.close() 
print(my_out)

with open(os.environ['EXP_PATH'], 'r') as exp_h:
	my_exp = exp_h.readline()
	exp_h.close() 

def my_sol_check(exo, exp):
    with open(exo, 'r') as the_in:
        with open(exp, "r") as the_out:
            l = the_in.readline()
            r = the_out.readline()
            diff = difflib.Differ().compare(r,l)
            the_in.close()
            the_out.close()
    return ''.join(diff)


print(my_sol_check(os.environ["OUTPUT_PATH"], os.environ["EXP_PATH"]))

