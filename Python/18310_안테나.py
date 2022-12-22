import sys

n = int(sys.stdin.readline())

house = list(map(int, sys.stdin.readline().split()))
house.sort()

le = (len(house) -1) // 2

print(house[le])
