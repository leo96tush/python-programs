import math
def findmax(n):
    if(math.sqrt(n)==int(math.sqrt(n))):
        k = int(math.sqrt(n))
    else:
        k = int(math.sqrt(n))+1
    for i in range(k,n+1):
        if(n%i==0):
            return(i)
            break

n = int(input())
arr = [0]*(n+1)

for i in range(n+1):
    if(i==0):
        arr[0] = 0
    elif(i==1):
        arr[1] = 1
    elif(i==2):
        arr[2] = 2
    elif(i==3):
        arr[3] = 3
    else:
        k = findmax(i)
        if(i!=findmax(i)):
            arr[i] = min(1+arr[i-1],1+arr[k])
        else:
            arr[i] = 1+arr[i-1]
print(arr[n])



