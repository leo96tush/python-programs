#code
def factorial(n):
    fact = 1
    if(n==0 or n==1):
        return(fact)
    else:
        while(n>0):
            fact = fact*n
            n = n - 1
        return(fact)
for _ in range(int(input())):
    n = int(input())
    m = list(str(factorial(n)))
    k = m[::-1]
    for i in range(len(k)):
        if(k[i]!='0'):
            print(k[i])
            break
