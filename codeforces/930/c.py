import math
import sys

t = int(input())

for _ in range(t):
    n = int(input())
    full = 0
    temp = 1
    while temp < n:
        temp *= 2
    
    if temp == n:
        full = 1
        # print("full")

    # find max
    max_candidate = 0
    for i in range(n):
        print(f"? {max_candidate} {max_candidate} {i} {i}")
        info = input().strip()
        if info == "<":
            max_candidate = i
        else:
            continue
    
    if full:
        min_candidate = 0
        for i in range(n):
            print(f"? {min_candidate} {min_candidate} {i} {i}")
            info = input().strip()
            if info == ">":
                min_candidate = i
            else:
                continue
        print(f"! {min_candidate} {max_candidate}")
    else:
        partner = 0
        partner_lst = []
        for i in range(n):
            print(f"? {max_candidate} {partner} {max_candidate} {i}")
            info = input().strip()
            if info == "<":
                partner = i
            else:
                continue
        
        print(f"! {partner} {max_candidate}")
    
    # print("\n")
    # sys.stdout.flush()

