#py-basic-data-types.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/list-comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    arr=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(arr)
    
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    first = -101
    second = -101
    for i in arr:
        if i>first:
            second = first
            first = i
        elif i<first and i>second:
            second = i
    print(second)

#https://www.hackerrank.com/challenges/nested-list
if __name__ == '__main__':
    first=[["",101.0]]
    second=[["",101.0]]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if (score==first[0][1]):
            first.append([name,score])
        elif (score<first[0][1]):
            second = first
            first = [[name,score]]
        elif (score>first[0][1] and score<second[0][1]):
            second = [[name,score]]
        elif (score>first[0][1] and score==second[0][1]):
            second.append([name,score])
    result=[]
    for s in second:
        result.append(s[0])
    result.sort()
    for r in result:
        print(r)

#https://www.hackerrank.com/challenges/finding-the-percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s = student_marks[query_name]
    print("%.2f" % (sum(s)/3))

#https://www.hackerrank.com/challenges/python-lists
if __name__ == '__main__':
    N = int(input())
    m=[]
while True:
    try:
        arr = list(input().rstrip().split())
        if arr[0] == 'insert':
            m.insert(int(arr[1]),int(arr[2]))
        elif arr[0] == 'print':
            print(m)
        elif arr[0] == 'remove':
            m.remove(int(arr[1]))
        elif arr[0] == 'append':
            m.append(int(arr[1]))
        elif arr[0] == 'sort':
            m.sort()
        elif arr[0] == 'pop':
            m.pop()
        elif arr[0] == 'reverse':
            m.reverse()      

    except:
        break

#https://www.hackerrank.com/challenges/python-tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

#
#
#
#
#

#
#
#
#
#
#
