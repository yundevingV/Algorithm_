import sys
n = int(sys.stdin.readline())
a = [0]*10000
for _ in range(n):
    num = int(sys.stdin.readline())
    a[num]+= 1  
for i in range(10000):
  if a[i] != 0:
    for j in range(a[i]):
      print(i+1)