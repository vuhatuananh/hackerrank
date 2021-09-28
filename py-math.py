#py-math.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/polar-coordinates
import cmath
e = complex(input())
r,p = cmath.polar(e)
print(r)
print(p)

#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())
print(str(int(round(math.degrees(math.atan(ab/bc)))))+"°")

#https://www.hackerrank.com/challenges/triangle-quest-2/problem?isFullScreen=true
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i-1)//9)**2)

#https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true
## Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a,b))

#https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b, m = int(input()), int(input()), int(input())
print(pow(a,b))
print(pow(a,b,m))

#https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b, c, d = (int(input()) for _ in range(4))
print(pow(a,b)+pow(c,d))

#https://www.hackerrank.com/challenges/python-quest-1/problem?isFullScreen=true
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(round((10**i-1)/9*i))

#
#
#
#
#
#
#
