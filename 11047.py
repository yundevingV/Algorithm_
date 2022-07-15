import sys
list=[]
count =0;
num,price = [int(x) for x in sys.stdin.readline().split()]

num = int(num)
price = int(price)
for i in range(num):
    c = int(input(''))
    list.append(c)

if price > 0:
    for i in range(num-1,-1,-1) :
        if price >= list[i] :
            ca = price // list[i]
            price = price - (list[i]*ca)
            count+=ca
            

print(count)