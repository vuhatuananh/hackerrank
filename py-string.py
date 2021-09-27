#py-string.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/swap-case
def swap_case(s):
    r=""
    for i in range(len(s)):
        if s[i].isalpha():
            if ord(s[i])<97: r+=chr(ord(s[i])+32)
            else: r+=chr(ord(s[i])-32)
        else:
            r+=s[i]

    return r
    
#https://www.hackerrank.com/challenges/python-mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
    
#https://www.hackerrank.com/challenges/find-a-string
def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string.startswith(sub_string,i) > 0: count+=1
    return count

#https://www.hackerrank.com/challenges/string-validators
if __name__ == '__main__':
    s = input().strip()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in range(len(s)):
        if not alnum and s[i].isalnum(): alnum = True
        if not alpha and s[i].isalpha(): alpha = True
        if not digit and s[i].isdigit(): digit = True
        if not lower and s[i].islower(): lower = True
        if not upper and s[i].isupper(): upper = True

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

#https://www.hackerrank.com/challenges/text-wrap
def wrap(string, max_width):
    r = ""
    for i in range(0,len(string),max_width):
        r += string[i:i+max_width] + "\n"
    return r

#https://www.hackerrank.com/challenges/python-string-formatting
def print_formatted(number):
    # your code goes here
    b = bin(number)
    l = len(b.lstrip('-0b'))
    for i in range(1,number+1):
        print("{:>{width}d}".format(i, width=l), end=" ")
        print("{:>{width}o}".format(i, width=l), end=" ")
        print("{:>{width}X}".format(i, width=l), end=" ")
        print("{:>{width}b}".format(i, width=l))

        
#https://www.hackerrank.com/challenges/alphabet-rangoli
import string

def rangoli(begin, size):
    a = list(string.ascii_lowercase)
    s = a[begin-1]
    if begin==size: 
        return s
    else:
        for i in range(begin, size):
            s = '-' + s + '-'
            s = a[i] + s + a[i]
    return s

def print_rangoli(size):
    # your code goes here

    for i in range(size,0,-1):
        r = rangoli(i,size)
        print(r.center((size-1)*4+1,'-'))

    for i in range(2,size+1):
        r = rangoli(i,size)
        print(r.center((size-1)*4+1,'-'))

# Complete the solve function below.
def solve(string):
    for s in string.split():
        string = string.replace(s, s.capitalize())
    return string

#https://www.hackerrank.com/challenges/the-minion-game
def minion_game(string):
    # your code goes here
    s, k = 0, 0
    l = len(string)
    for i in range(l):
        if string[i] in ["U","E","O","A","I"]:
            k += l-i
        else:
            s += l-i
    if s>k:
        print("Stuart", s)
    elif s<k:
        print("Kevin", k)
    else:
        print("Draw")
        
#https://www.hackerrank.com/challenges/merge-the-tools
def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    for i in range(n//k):
        r = []
        for j in range(k):
            if string[i*k+j] not in r:
                r.append(string[i*k+j])
        print("".join(r))

#
#
#
#
#
