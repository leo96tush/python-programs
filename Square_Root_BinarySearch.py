def sqrt(A):
    if(A==0 or A==1):
        return(A)
    else:
        low = 2
        high = A//2
        mid = (low+high)//2
        while(low<=high):
            mid = (low+high)//2
            if(mid*mid==A):
                return(mid)
            elif(mid*mid>A):
                high = mid-1
            else:
                low = mid+1
        if(mid*mid>A):
            mid = mid-1
        return(mid)

n = int(input())
print(sqrt(n))
