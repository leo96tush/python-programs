n = int(input())
arr = list(map(int,input().split()))

if(len(arr)%2==0):
    arr_1 = sorted(arr)
    k_1 = arr_1[(len(arr_1)//2)-1]
    k_2 = arr_1[(len(arr_1)//2)]
    cost_1 = 0
    cost_2 = 0
    for i in range(len(arr_1)):
        cost_1 = cost_1 + abs(arr_1[i]-k_1)
        cost_2 = cost_2 + abs(arr_1[i]-k_2)
    print(min(cost_2,cost_1))
else:
    arr_1 = sorted(arr)
    k_1 = arr_1[(len(arr_1)//2)]
    cost = 0
    for i in range(len(arr_1)):
        cost = cost + abs(arr_1[i]-k_1)
    print(cost)
