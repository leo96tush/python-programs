for _ in range(int(input())):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    count = list()
    for i in range(len(arr)):
        k = (arr[i]+x)//2
        m = 0
        for j in range(len(arr)):
            if(arr[j]==k):
                m=m+1
        count.append(m)

    print(*count,sep=' ')
