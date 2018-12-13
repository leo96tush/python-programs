import math
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    a = list()
    b = list()
    for i in range(n):
        if(i%2==0):
            a.append(arr[i])
        else:
            b.append(arr[i])

    c = a[::-1]
    d = b[::-1]
    x = 0
    y = 0
    for i in range(len(c)):
        x = x + (c[i]*math.pow(10,i))
    for i in range(len(d)):
        y = y + (d[i]*math.pow(10,i))

    print(int(x+y))
