m = int(input())
r = 0
for r in range(m):
    n = int(input())
    q = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr3 = list(map(int,input().split()))
    x = list()
    y = list()
    z = list()
    l = list()
    r = list()
    k = list()
    stud = list()
    x.append(arr1[0])
    x.append(arr1[1])
    y.append(arr2[0])
    y.append(arr2[1])
    z.append(arr3[0])
    z.append(arr3[1])
    for i in range(2,n+1):
        x.append(arr1[2]*x[i-2]+arr1[3]*x[i-3]+arr1[4])%arr1[5]
    for i in range(2,n+1):
        y.append(arr2[2]*y[i-2]+arr2[3]*y[i-3]+arr2[4])%arr2[5]
    for i in range(2,n+1):
        z.append(arr3[2]*y[i-2]+arr3[3]*y[i-3]+arr3[4])%arr3[5]
    for i in range(n):
        l.append(min(x[i],y[i]))
        r.append(max(x[i],y[i]))
        stud.append(r[i]-l[i]+1)
    for i in range(q):
        k.append(z[i]+1)
        
