def factorial(n):
    fact = 1
    if(n==1 or n==0):
        return(1)
    else:
        while(n>0):
            fact = fact*n
            n = n-1
        return(fact)

n = int(input())
print(factorial(n))
