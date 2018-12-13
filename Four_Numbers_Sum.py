for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr_1 = sorted(arr)
    count=0
    for i in range(len(arr)-1):
        if(abs(arr_1[i+1]-arr_1[i])<=1):
            count=count+1
    if(count==(len(arr)-1)):
        print('Yes')
    else:
        print('No')
