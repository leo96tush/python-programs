def rotate(a):
    k = a[0]
    a.remove(k)
    a.append(k)
    return(a)

n = int(input())
a = list(map(int,input().split()))
print(*rotate(a),sep=' ')