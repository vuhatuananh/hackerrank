#py-collections.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/collections-counter
import collections
_ = int(input())
shoes = list(map(int, input().split()))
store = collections.Counter(shoes)
N = int(input())
S = 0;
for _ in range(N):
    size, price = map(int, input().split())
    if store[size]>0:
        S += price
        store[size] -= 1
print(S)

#https://www.hackerrank.com/challenges/defaultdict-tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
import collections
n,m = map(int, input().split())
A = list(input() for _ in range(n))
B = list(input() for _ in range(m))
d = collections.defaultdict(list)

for i in range(n):
    d[A[i]].append(i+1)

for i in range(m):
    if B[i] in d:
        print(*d[B[i]])
    else:
        print("-1")

#https://www.hackerrank.com/challenges/py-collections-namedtuple
import collections
n = int(input())
Student = collections.namedtuple("Student", input())
S = (Student(*input().split()) for _ in range(n))
print("{:.2f}".format(sum(int(s.MARKS) for s in S)/n))

#https://www.hackerrank.com/challenges/py-collections-ordereddict
import collections
n = int(input())
d = collections.OrderedDict()
for _ in range(n):
    key, value = input().rsplit(" ", 1)
    if key not in d:
        d[key] = int(value)
    else:
        d[key] += int(value)

[print(k, v) for k, v in d.items()]

#https://www.hackerrank.com/challenges/word-order
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections 
n = int(input())
S = [input() for _ in range(n)]
C = collections.Counter(S)
print(len(C))
print(*C.values())

#https://www.hackerrank.com/challenges/py-collections-deque
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
n = int(input())
d = collections.deque()
for _ in range(n):
    c, *arg = input().split()
    getattr(d, c)(*arg)

print(*d)

#https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    s = input()
    c = collections.Counter(s)
    for k, v in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(k, v)

#https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
T = int(input())

for _ in range(T):
    m = 2**31
    r = "Yes"
    n = int(input())
    d = collections.deque([int(x) for x in input().split()])
    for i in range(len(d)):
        if d[0]>d[-1]:
            c = d.popleft()
        else: 
            c = d.pop()
        if c<=m:
            m=c
        else:
            r="No"
            break
    print(r)



#
#
#
#
