import sys

n,m = map(int, sys.stdin.readline().split())

a = set(map(int, sys.stdin.readline().split()))

b = set(map(int, sys.stdin.readline().split()))

ab = a-b
ba = b-a

print(len(ab) + len(ba))