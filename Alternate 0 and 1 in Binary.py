def alternate(n):
    x = bin(n)[2:]
    a = list(x)
    for i in range(1,len(x)):
        if(a[i-1]==a[i]):
            return('No')
            break
    else:
        return('Yes')



k = int(input())
print(alternate(k))