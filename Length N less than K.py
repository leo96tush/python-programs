A = list(map(int,input().split()))
B = int(input())
C = int(input())
count = 0
for i in range(len(A)):
    A[i] = str(A[i])

P = list(A)
for i in range(C):
    k = list(str(i))
    print(k)0 
    if(len(k)==B):
        for j in P:
            if j in k:
                count = count+1
            else:
                pass
print(count)