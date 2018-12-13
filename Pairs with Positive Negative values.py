for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    a = sorted(arr)
    c = list()
    d = list()
    e = list()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(a[i]==(-1)*a[j] and i<j):
                c.append(a[i])
                d.append(a[j])
                
    #c = c[::-1]
    #d = d[::-1]
    print(c)
    print(d)
    for i in range(len(c)):
        e.append(c[len(c)-i-1])
        e.append(d[len(d)-i-1])
    
    if(len(e)==0):
        print("0")
    else:
        print(e)
    


