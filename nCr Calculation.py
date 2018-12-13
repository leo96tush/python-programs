def factorial(num):
    fact = 1
    while(num>0):
        fact = fact*num
        num = num-1
    return(fact)

for _ in range(int(input())):
    n,r = list(map(int,input().split()))
    print(factorial(n)//(factorial(n-r)*factorial(r)))
        
    
