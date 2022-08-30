import sys

n = int(sys.stdin.readline())

lst = []

lst = list(map(int, sys.stdin.readline().split()))


lst.sort()

#size(Fi) ≤ size(Fj)이면서, size(Fi) ≥ 0.9 × size(Fj)


print(lst)