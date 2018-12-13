for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    m = 0
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if( (a[i]+a[j]>a[k]) and (a[j]+a[k]>a[i]) and (a[k]+a[i]>a[j]) and (i<j) and (j<k)):
                    r = a[i]+a[j]+a[k]
                    if(r>m):
                        m = r
                        
    if(m>0):
        print(m)
    else:
        print('-1')
