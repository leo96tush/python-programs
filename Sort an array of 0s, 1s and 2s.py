for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    a = list()
    for i in range(n):
        if(arr[i]==0 or arr[i]==1 or arr[i]==2):
            a.append(str(arr[i]))
            
    print(' '.join(sorted(a)))
