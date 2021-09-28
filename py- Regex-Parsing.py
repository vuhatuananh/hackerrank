#py- Regex-Parsing.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/introduction-to-regex
import re
for _ in range(int(input())):
    s = input()
    p = r"^[\+-]?\d*\.\d+$"
    m = re.match(p, s)
    print(bool(m))

#https://www.hackerrank.com/challenges/re-split
regex_pattern = r"[,\.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#https://www.hackerrank.com/challenges/re-group-groups
import re
s = input().strip()
p = r"([a-zA-Z0-9])\1"
m = re.search(p,s)
print(m.group(1) if m else -1)


#https://www.hackerrank.com/challenges/re-findall-re-finditer
import re
m = re.finditer(r"([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]*)([ueoaiUEOAI][ueoaiUEOAI]+)([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]*)", input().strip())
print("\n".join(map(lambda x: x.group(2), m)) if m else -1)

#https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
import re
S, k = input().strip(), input().strip()
matches = re.finditer(r"(?=({}))".format(k), S)
if k not in S:
    print("(-1, -1)")
else:
    print(*[(m.start(1), m.end(1)-1) for m in matches], sep="\n")

#https://www.hackerrank.com/challenges/re-sub-regex-substitution
import re
n = int(input())
for i in range(n):
    s = input()
    ra = re.sub(r"(?<= )&&(?= )", "and", s)
    ro = re.sub(r"(?<= )\|\|(?= )", "or", ra)
    print(ro)

#https://www.hackerrank.com/challenges/validate-a-roman-number
regex_pattern = r"(?<=^)(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?=$)"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#
#
#
#
#
