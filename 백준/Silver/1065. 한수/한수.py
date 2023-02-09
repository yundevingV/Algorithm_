import sys

# n = int(sys.stdin.readline())

# #111 123 135 147 159 

# #222 234 246 258 210 

# #333 345 357 369 321 

# #444 456 468 432 420 

# #555 567 579 543 531 

# #666 678 654 642 630 

# #777 789 765 753 741 

# #888 876 864 852 840 

# #999 987 975 963 951 

# count = 0
# for i in range(1,n+1) :
#     if i < 100 :
#         count +=1
#     elif i == 111 or i == 123 or i == 135 or i == 147 or i == 159 :
#         count +=1
#     elif i == 222 or i == 234 or i == 246 or i == 258 or i == 210 :
#         count +=1
#     elif i == 333 or i == 345 or i == 357 or i == 369 or i == 321 :
#         count +=1
#     elif i == 444 or i == 456 or i == 468 or i == 432 or i == 420 :
#         count +=1
#     elif i == 555 or i == 567 or i == 579 or i == 543 or i == 531 :
#         count +=1
#     elif i == 666 or i == 678 or i == 654 or i == 642 or i == 630 :
#         count +=1
#     elif i == 888 or i == 876 or i == 864 or i == 852 or i == 840 :
#         count +=1
#     elif i == 999 or i == 987 or i == 975 or i == 963 or i == 951 :
#         count +=1
#     elif i == 777 or i == 789 or i == 765 or i == 753 or i == 741 :
#         count +=1
    
        
    
inpu = input()

num = int(inpu)

count = 0
for i in range(1,num+1) :
    if i < 100 :
        count+=1
    else :
        stri = str(i)
        if  int(stri[0]) - int(stri[1]) == int(stri[1]) - int(stri[2]) :
            count +=1
        else :
            count +=0
        
print(count)