import sys

n, m = map(int, sys.stdin.readline().split())

score = list(map(int, sys.stdin.readline().split()))
score.sort()

print(score[-m])
