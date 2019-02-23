#!/bin/python3

import os
import sys

def setWorkSpace():
    for f in os.environ["OUTPUT_PATH"].split():
        print(f)
        if os.path.isfile(f): 
            os.remove(f)

# def my_sol_check(in_f, out_f):
#     with open(in_f, 'r') as the_in:
#         with open(out_f, "w") as the_out:
#             while the_in.readline() = l :

import difflib
def my_sol_check(exo, exp):
    with open(exo, 'r') as the_in:
        with open(exp, "r") as the_out:
            l = the_in.readline()
            r = the_out.readline()
            diff = difflib.Differ().compare(r,l)
            the_in.close()
            the_out.close()
            return ''.join(diff)
    
