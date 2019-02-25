# https://www.hackerrank.com/challenges/staircase/

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setup import *

os.environ["INPUT_PATH"] = "bla.in"
os.environ["OUTPUT_PATH"] = "bla.out"
os.environ["EXP_PATH"] = "bla.exp"


setWorkSpace()
from functools import reduce
def problem(ar):