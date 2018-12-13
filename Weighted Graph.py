n = int(input())

a = [ [ 0 for i in range(n)] for j in range(n)]


for i in range(n):
    for j in range(n):
        if(i==j):
            a[i][j]==0
        else:
            i,j,a[i][j] = int(input()),int(input()),int(input())

print(a)
