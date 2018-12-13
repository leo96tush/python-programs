def rotate(arr):
    k = len(arr)
    m = arr[len(arr)-1]
    arr.insert(0,m)
    arr = arr[0:k]
    return(arr)
def delete_element(arr,i):
    k = len(arr)-1
    if(i>k):
        arr = arr[1:]
    else:
        del(arr[len(arr)-i-1])
    return(arr)
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
        #if(len(arr)==1):
            #break
        #else:
    for i in range(2**n):
        if(len(arr)==1):
            break
        else:
            arr = rotate(arr)
            arr = delete_element(arr,i)
    print(*arr)
    


    
    
