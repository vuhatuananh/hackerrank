#py-sets.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/py-introduction-to-sets
import math

def average(array):
    # your code goes here
    s = set(array)
    return sum(s)/len(s)
    
#https://www.hackerrank.com/challenges/no-idea
# Enter your code here. Read input from STDIN. Print output to STDOUT
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
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nn = set(map(int,input().strip().split()))
m = int(input())
mm = set(map(int, input().strip().split()))
rr = nn ^ mm

for r in sorted(rr):
    print(r)










