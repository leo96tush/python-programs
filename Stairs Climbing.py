def factorial(n):
    fact = 1
    if(n==0 or n==1):
        return(int(1))
    else:
        for i in range(2,n+1):
            fact = fact*i
        return(fact)
    
def comb(n,r):
    return(factorial(n)//(factorial(r)*factorial(n-r)))

n = int(input())
#Number of 1's = n1
#Number of 2's = n2
count = 0
if((n%2)==0):
    for i in range(0,(n//2)+1):
        n1 = 2*i
        n2 = (n-n1)//2
        count = count + comb((n1+n2),n1)
    print(count)
else:
    for i in range(0,(n//2)+1):
        n1 = 2*i+1
        n2 = (n-n1)//2
        count = count + comb((n1+n2),n1)
    print(count)
