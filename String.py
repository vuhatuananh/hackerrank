#https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    r=""
    for i in range(len(s)):
        if s[i].isalpha():
            if ord(s[i])<97: r+=chr(ord(s[i])+32)
            else: r+=chr(ord(s[i])-32)
        else:
            r+=s[i]

    return r
    
#https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
    
#https://www.hackerrank.com/challenges/find-a-string/submissions/code/182456312
def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string.startswith(sub_string,i) > 0: count+=1
    return count
