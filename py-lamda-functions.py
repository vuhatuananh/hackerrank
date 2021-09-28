#py-lamda-functions.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/map-and-lambda-expression
cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-2]+fib[i-1])
    return fib[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter
import re
def fun(s):
    # return True if s is a valid email, else return False
    return re.match(r"^[a-z][\w-]*@[a-z0-9]+\.[a-z]{1,3}$", s, re.I)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

#https://www.hackerrank.com/challenges/reduce-function
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
    
#
#
#
#
#
