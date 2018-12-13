def isprime(num):
    for i in range(2,num):
        if(num%i==0):
            return(False)
            break
    else:
        return(True)

n = int(input())
print(isprime(n))
        
