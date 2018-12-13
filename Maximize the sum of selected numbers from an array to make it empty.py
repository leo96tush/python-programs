def maxsum(a,n):
    if(len(a)>1):
        p = a.index(max(a))
        k = max(a)
        if(p==(len(a)-1)):
            a.remove(a[len(a)-1])
            a.remove(a[len(a)-1])
            return(k+maxsum(a,n-2))
        elif(p==0):
            a.remove(a[0])
            return(k+maxsum(a,n-1))
        else:
            a.remove(a[p-1])
            a.remove(a[p-1])
            return(k+maxsum(a,n-2))
    else:
        return(int(a[0]))
        
    

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(maxsum(a,n))