import sys

test = int(sys.stdin.readline())

for i in range(test) :
    count = 0

    n,m = [int(x) for x in sys.stdin.readline().split()]
    num_list = list(map(int, input().split()))
    result = num_list[m]
    check_list = [0 for _ in range(n)]
    check_list[m] = 1
    dict = {}
    for k in num_list :
        dict[k] =0
    print(dict)


    # while True :
    #     for j in num_list :
    #         p = max(num_list)
    #         if j == p :



