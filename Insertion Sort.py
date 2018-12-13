n = int(input('The number of elements: '))
arr = list()
for i in range(n):
    k = int(input())
    arr.append(k)
    arr = sorted(arr)

print(arr)
