import sys

x, y, w, h = map(int, sys.stdin.readline().split())

yh = min((y-0),(h-y))
xw = min((x-0),(w-x))

print(min(yh,xw))