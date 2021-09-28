#py-itertools.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/itertools-product
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(itertools.product(A,B))
for c in C:
    print(c, end=" ")

#https://www.hackerrank.com/challenges/itertools-permutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
S, N = input().split()
n = int(N)
SS = list(itertools.permutations(S, n))
SS.sort()
for s in SS:
    for i in range(n):
        print(s[i], end="")
    print()

#https://www.hackerrank.com/challenges/itertools-combinations
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
S, k = input().split()
SS = list(S)
SS.sort()
k = int(k)
for i in range(1,k+1):
    R = list(itertools.combinations(SS,i))
    R.sort()
    for j in range(len(R)):
        P = "".join(R[j])
        print(P)

#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
S, k = input().split()
SS = list(S)
SS.sort()
k = int(k)
R = list(itertools.combinations_with_replacement(SS,k))
R.sort()
for i in range(len(R)):
    print("".join(R[i]))

#https://www.hackerrank.com/challenges/compress-the-string
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

for k,g in itertools.groupby(input()):
    print("({}, {})".format(len(list(g)), k), end=" ")

#https://www.hackerrank.com/challenges/iterables-and-iterators
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
n = int(input())
s = input().split()
k = int(input())
comb = list(itertools.combinations(s,k))

f = [c for c in comb if "a" in c]

print(len(f)/len(comb))

#https://www.hackerrank.com/challenges/maximize-it
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
K, M = map(int, input().split())
X = (list(map(int, input().split()))[1:] for _ in range(K))
R = (list(map(lambda x: sum(i*i for i in x)%M, itertools.product(*X))))
print(max(R))

