def digitsum(num):
    n = num
    sum = 0
    while(n>0):
        res = n%10
        sum = sum + res
        n = n//10
    return(sum)
    
def prodnum(num):
    n = num
    prod = 1 
    while(n>0):
        res = n%10
        prod = prod*res
        n = n//10
    return(prod)
        
def calculate(num):
    if( digitsum(num)>=10):
        return(calculate(digitsum(num)))
    else:
        return(prodnum(num))

for _ in range(int(input())):
    n = int(input())
    print(calculate(n))
