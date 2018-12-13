def swap(a,b):
    t = a
    a = b
    b = t
    return(a,b)

m = int(input())
n = int(input())
print(swap(m,n))
