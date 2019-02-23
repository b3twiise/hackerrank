# https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=next-challenge&h_v=zen

import sys
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setup import *
os.environ['OUTPUT_PATH'] = "compare_the_triplets.0.out compare_the_triplets.1.out"
os.environ['INPUT_PATH'] = "compare_the_triplets.0.in compare_the_triplets.1.in"
os.environ['EXPECT_PATH'] = "compare-the-triplets.0.exp compare_the_triplets.1.exp"

setWorkSpace()

def compare_the_triplets(arr1, arr2):
	ret = []
	alice = 0
	bob = 0
	i = 0
	while i < len(arr1):
		if arr1[i] >  arr2[i]:
			alice += 1
		elif arr1[i] < arr2[i]:
			bob += 1
		i += 1
	return[alice, bob]

# print(os.environ['INPUT_PATH'].split()[0])



for i in range(len(os.environ['INPUT_PATH'].split())):
	my_res = None
	in_f, out_f = os.environ['INPUT_PATH'].split()[i], os.environ['OUTPUT_PATH'].split()[i]
	exp_f = in_f[:-2] + "exp"

	with open(in_f, 'r') as in_ptr:
		with open(out_f, 'w') as out_ptr:
			arr1 = list(map(int, in_ptr.readline().split()))
			arr2 = list(map(int, in_ptr.readline().split()))
			my_res = compare_the_triplets(arr1, arr2)
			print(my_res)
			out_ptr.write(str(my_res))
			




	res = my_sol_check(out_f, exp_f)
	print(res)
	
	# with open(in_f, 'r') as in_ptr:
	# 	with open(out_f, 'w') as out_ptr:
	# 		with open(exp_f, "r") as exp_ptr:

	# 			arr1 = list(map(int, in_ptr.readline().split()))
	# 			arr2 = list(map(int, in_ptr.readline().split()))

	# 			my_res = compare_the_triplets(arr1, arr2)
	# 			out_ptr.write(str(my_res))
	# 			in_ptr.close()
	# 			my_exp = list(map(int, exp_ptr.readline().split()))

	# 			print("Expected:",my_exp, "Got:",my_exp)