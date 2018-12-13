arr = list(map(int,input().split()))
b = int(input())

for i in range(len(arr)):
    if (arr[i]==b):
        b = 2*b
print(b)
