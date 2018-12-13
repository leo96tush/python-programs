n = int(input())
prime = []
non_prime = []
non_prime.append(1)
prime.append(2)
for i in range(3,n):
    if(((i%j)==0) for j in prime):
        non_prime.append(i)
    elif((((i%j)==0) for j in non_prime) and j!=1):
        non_prime.append(i)
    else:
        prime.append(i)

print(prime)
print(non_prime)