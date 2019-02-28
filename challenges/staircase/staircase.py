# https://www.hackerrank.com/challenges/staircase/

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setup import *

os.environ["INPUT_PATH"] = "bla.in"
os.environ["OUTPUT_PATH"] = "bla.out"
os.environ["EXP_PATH"] = "bla.exp"


setWorkSpace()
from functools import reduce
def staircase(n):
	str_res = ""
	res = []
	for i in range(n):
		res.append(" " * (n - i -1) + "#" * (i +1))
		# res.append(" "* i + "#" * n - i)
	for i in res:
		if i != "#" * (len(res)):

			str_res += i + "\n"

	str_res += i
	return str_res

# [print(l, file=open(os.environ["OUTPUT_PATH"], "a"))for l in staircase(4)]


[print(staircase(6), file=open(os.environ["OUTPUT_PATH"], "a"))]



judge("bla.out", "bla.exp")