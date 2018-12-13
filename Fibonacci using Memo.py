fib_cache = {}

def fib(n):
    if n in fib_cache:
        return(fib_cache[n])

    if(n==1 or n==0):
        return(1)
    else:
        value = fib(n-1)+fib(n-2)
        fib_cache[n] = value
        return(value)

for i in range(1,301):
    print(i,':',fib(i))
    
https://about.yahoo.co.jp/hr/
