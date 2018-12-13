for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = list()
    d = list()
    e = list()
    for i in range(len(a)):
        if(a[i]<0):
            c.append(a[i])
        else:
            d.append(a[i])


    for i in range(len(c)):
        e.append(str(d[i]))
        e.append(str(c[i]))

    print(' '.join(e))
