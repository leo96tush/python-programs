def binary_search(arr,low,high,k):
    if(high>=low):
        mid = low + (high-low)//2
        if(arr[mid]==k):
            return(mid)
        elif(arr[mid]>k):
            return(binary_search(arr,low,mid-1,k))
        else:
            return(binary_search(arr,mid+1,high,k))
    else:
        return(-1)
    
    
    
arr = list(map(int,input().split()))
value = int(input())
print(binary_search(arr,0,len(arr),value))
