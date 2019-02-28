# https://www.hackerrank.com/challenges/mini-max-sum/problem?
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setup import *


truncated = "miniMaxSum"
os.environ["INPUT_PATH"] = truncated +".in"
os.environ["OUTPUT_PATH"] = truncated + ".out"
os.environ["EXP_PATH"] = truncated + ".exp"


setWorkSpace()
from functools import reduce


def miniMaxSum(ar):
	ar = sorted(ar)
	return [sum(ar[:-1]), sum(ar[1:])]
	

print(miniMaxSum([1,2,3,4,5]))