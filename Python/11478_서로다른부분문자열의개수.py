import sys

s = (sys.stdin.readline().rstrip())


sets = set()

for i in range(len(s)) :
    for j in range(i,len(s)) :
        sets.add(s[i:j+1])


print(len(sets))