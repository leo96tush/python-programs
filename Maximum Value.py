def maxprod(n):
    max_value = 1
    if(n==1):
        return(max_value)
    else:
        max_val = 0
        for i in range(1,n-1):
            max_val=max(max_val,max((i*(n-i)),maxprod(n-i)*i))
    
    return(max_val)



n = int(input())
print(maxprod(n))
