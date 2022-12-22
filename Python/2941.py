import sys

str = (sys.stdin.readline().strip())

lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in lst :
    str = str.replace(i,'!')

print(len(str))


