
# https://www.hackerrank.com/challenges/a-very-big-sum
import sys

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setup import *

os.environ["INPUT_PATH"] = "a_very_big_sum.in"
os.environ["OUTPUT_PATH"] = "a_very_big_sum.out"
os.environ["EXP_PATH"] = "a_very_big_sum.exp"


setWorkSpace()
from functools import reduce
def aVeryBigSum(ar):
	return reduce(lambda x, y: x + y, ar)

my_in = my_out = my_exp = None
with open(os.environ['INPUT_PATH'], 'r') as read_h:
	c = read_h.readline()
	my_in = list(map(int, read_h.readline().split()))
	read_h.close()

with open(os.environ['OUTPUT_PATH'], 'w') as write_h:
	my_out = aVeryBigSum(my_in)
	write_h.write(str(my_out))
	write_h.close() 
with open(os.environ['EXP_PATH'], 'r') as exp_h:
	my_exp = exp_h.readline()
	exp_h.close() 
print("my_out:", my_out)
print("my_exp:", my_exp)