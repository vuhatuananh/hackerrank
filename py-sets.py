#py-sets.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/py-introduction-to-sets
import math

def average(array):
    # your code goes here
    s = set(array)
    return sum(s)/len(s)
    
#https://www.hackerrank.com/challenges/no-idea
n, m = map(int, input().strip().split())
N = list(map(int, input().strip().split()))
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))
h = 0

for i in N:
    if i in A:
        h+=1

for j in N:
    if j in B:
        h-=1

print(h)

#https://www.hackerrank.com/challenges/symmetric-difference
n = int(input())
nn = set(map(int,input().strip().split()))
m = int(input())
mm = set(map(int, input().strip().split()))
rr = nn ^ mm

for r in sorted(rr):
    print(r)

#https://www.hackerrank.com/challenges/py-set-add
n = int(input())
ss = set()
for _ in range(n):
    s = input()
    ss.add(s)
print(len(ss))

#https://www.hackerrank.com/challenges/py-set-discard-remove-pop
n = int(input())
s = set(map(int, input().split()))
m = int(input())
while True:
    try:
        c = input().strip().split()
        if c[0]=="pop": s.pop()
        elif c[0]=="remove": s.remove(int(c[1]))
        elif c[0]=="discard": s.discard(int(c[1]))
    except:
        break
print(sum(s))

#https://www.hackerrank.com/challenges/py-set-union
n = int(input())
N = set(map(int, input().strip().split()))
m = int(input())
M = set(map(int, input().strip().split()))

print(len(N|M))

#https://www.hackerrank.com/challenges/py-set-intersection-operation
n = int(input())
A = set(map(int, input().strip().split()))
m = int(input())
B = set(map(int, input().strip().split()))

print(len(A&B))

#https://www.hackerrank.com/challenges/py-set-difference-operation
n = int(input())
A = set(map(int, input().strip().split()))
m = int(input())
B = set(map(int, input().strip().split()))
print(len(A-B))

#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation
n = int(input())
A = set(map(int, input().strip().split()))
m = int(input())
B = set(map(int, input().strip().split()))
print(len(A^B))

#https://www.hackerrank.com/challenges/py-set-mutations
a = int(input())
A = set(map(int, input().strip().split()))
n = int(input())
for _ in range(n):
    c = input().strip().split()[0]
    B = set(map(int, input().strip().split()))
    #if c == "intersection_update": A&=B
    #elif c == "symmetric_difference_update": A^=B
    #elif c == "difference_update": A-=B
    getattr(A, c)(B)

print(sum(map(int, A)))

#https://www.hackerrank.com/challenges/py-the-captains-room
n = int(input())
N = list(map(int, input().strip().split()))
D = {x:0 for x in set(N)}

for i in range(len(N)):
    D[N[i]] += 1

for k,v in D.items():
    if v==1:
        print(k)
        break

#https://www.hackerrank.com/challenges/py-check-subset
t = int(input())
for _ in range(t):
    a = int(input())
    A = set(map(int, input().strip().split()))
    b = int(input())
    B = set(map(int, input().strip().split()))
    print(not(A-B))

#https://www.hackerrank.com/challenges/py-check-strict-superset
A = set(map(int, input().strip().split()))
n = int(input())
superset = False
for i in range(n):
    B = set(map(int, input().strip().split()))
    if not(B-A):
        superset=False
        break
print(superset)

#
#
#
#
#
#









