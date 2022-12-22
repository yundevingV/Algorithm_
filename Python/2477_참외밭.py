import sys

n = int(sys.stdin.readline())

lst = []
widthIndex = 0
heightIndex = 0
widthIndexPivot = 0
heightIndexPivot = 0

for i in range(6) :
    arrow , length = map(int , sys.stdin.readline().split())
    lst.append((length,arrow))

for i in range(6) :
    if lst[i][1] == 1 or lst[i][1] == 2 :
        if heightIndexPivot < lst[i][0] :
            heightIndexPivot = lst[i][0]
            heightIndex = i

    elif lst[i][1] == 3 or lst[i][1] == 4 :
        if widthIndexPivot < lst[i][0] :
            
            widthIndexPivot = lst[i][0]
            widthIndex = i

height = abs(lst[(heightIndex+1)%6][0] - lst[(heightIndex-1)%6][0])
width = abs(lst[(widthIndex+1)%6][0] - lst[(widthIndex-1)%6][0])

square = height * width

bigSquare = lst[heightIndex%6][0] * lst[widthIndex%6][0]


result = bigSquare - square

print(result * n)
