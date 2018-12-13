def solve(arr):
    indexproduct = list()
    left = list()
    right = list()
    i = 0
    while(i<=(len(arr))):
        k = i+1
        j = i-1
        while(k<=(len(arr)-1)):
            if(arr[k]>arr[i]):
                right.append(k+1)
                break
            elif(arr[k]<=arr[i] and k==len(arr)):
                right.append(0)
                break
            else:
                k = k+1
        while(j>=0):
            if(arr[j]>arr[i]):
                left.append(j+1)
                break
            elif(arr[j]<=arr[i] and j==0):
                left.append(0)
                break
            else:
                j = j-1
        i = i+1
    print(left)
    print(right)
    for m in range(len(left)):
        indexproduct.append(left[m]*right[m])
    return(max(indexproduct))

n = int(input())
arr = list(map(int,input().split()))
print(solve(arr))