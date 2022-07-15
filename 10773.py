num = int(input())

list =[]
newlist =[]

for i in range(num) :
    a= int(input())
    list.append(a)

for j in range(len(list)) :
        jj = list[j]
        if jj != 0 :
            newlist.append(jj)
        else : 
            newlist.pop()

sum = 0

for k in range(len(newlist)) :
    sum += newlist[k]

print(sum)
