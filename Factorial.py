def factorial(n):
    fact = 1
    if(n==0 or n==1):
        return(fact)
    else:
        while(n>0):
            fact = fact*n
            n = n - 1
        return(fact)

n = int(input())
print(factorial(n))
        
