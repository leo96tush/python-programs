A = input().split()
B = input().split()

for i in B:
    A.remove(i)

print(' '.join(A))
