def isprime(num):
    for i in range(2,num+1):
        if(num%i==0):
            return(False)
        else:
            return(True)

n = int(input())
count  = 0
for i in range(n):
    if(isprime(i)==True):
        count = count + 1

print(count)
        
