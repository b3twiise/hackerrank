#link to problem
import sys

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setup import *

os.environ["INPUT_PATH"] = "plus_minus.in"
os.environ["OUTPUT_PATH"] = "plus_minus.out"
os.environ["EXP_PATH"] = "plus_minus.exp"


setWorkSpace()
# from functools import filter
from decimal import Decimal
def plusMinus(ar):
	# l = filter(lambda i: i < 0, ar)
	n = len(ar)
	poz, neg, heros = [i for i in filter(lambda i: i > 0, ar)], [i for i in filter(lambda i: i < 0, ar)], [ i for i in filter(lambda i: i == 0, ar)], 
	poz, neg, heros = format(Decimal(len(poz) / n), ".6f"), format(Decimal(len(neg)/n), ".6f") , format(Decimal(len(heros)/n), ".6f")
	return [poz, neg, heros]
	# return [poz, neg, heros]
arr = [-4, 3, -9, 0, 4, 1]





[print(i, file=open(os.environ["OUTPUT_PATH"], "a")) for i in plusMinus(arr)]


def direc_output(file, func):
	pass
def judge(orig, origg):
	f1=open(orig,"r")
	f2=open(origg,"r")
	for line1 in f1:
			for line2 in f2:
				if line1==line2:
					print("SAME\n")
					print(line2)
				else:
					print(line1 + line2)
				break
	f1.close()
	f2.close()


	# with open(orig) as f1, open(origg) as f2:
	# 	for l1, l2 in zip(f1, f2):
	# 		if l1 == l2:
	# 			print(l1, "==")
	# 			print(l2)
	# 		else:
	# 			print(l1, "#==")
	# 			print(l2)

judge(os.environ["EXP_PATH"], os.environ["OUTPUT_PATH"])