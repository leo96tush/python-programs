for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    arr = arr[::-1]
    b = list()
    for i in range(len(arr)-1):
        if(arr[i]==arr[i+1]):
            b.append(n-i-1)
            b.append(arr[i])
            break
        
    if(len(b)==0):
        b.append('-1')
        
    print(*b, sep=' ')
