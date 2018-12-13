for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    arr = sorted(list(map(int,input().split())))
    count = 0
    for i in range(n):
        if(m>0):
            m = m - arr[i]
            count = count+1
        else:
            break
    print(count-1)
