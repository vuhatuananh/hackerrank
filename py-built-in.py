#py-built-in.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/zipped
import collections
n, x = map(int, input().split())
#S = []
#for _ in range(x):
#    S.append(list(map(float, input().split())))
S = [list(map(float, input().split())) for _ in range(x)]
for z in zip(*S):
    print("{:.1f}".format(sum(z)/len(z)))

#https://www.hackerrank.com/challenges/input
x, k = map(int, input().split())
s = input()
print( eval(s) == k )

#https://www.hackerrank.com/challenges/python-eval
eval(input())

#https://www.hackerrank.com/challenges/python-sort-sort
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for s in sorted(arr, key=lambda x: x[k]):
        print(*s)
        
    #[print(*s) for s in sorted(arr, key=lambda x: x[k])]

#https://www.hackerrank.com/challenges/any-or-all
_, N = int(input()), list(map(int, input().strip().split()))
print(all([x>=0 for x in N]) and any([str(x)==str(x)[::-1] for x in N]))

#https://www.hackerrank.com/challenges/ginorts
S = input()
R = sorted([x for x in S if x.islower()]) + sorted([x for x in S if x.isupper()]) + sorted([x for x in S if x.isdigit() and int(x)%2==1]) + sorted([x for x in S if x.isdigit() and int(x)%2==0])
print("".join(R))

#
#
#
#
#
