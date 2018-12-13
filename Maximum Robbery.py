arr = list(map(int,input().split()))
sum1 = 0
sum2 = 0
for i in range(len(arr)):
    if(i%2==0):
        sum1 = sum1 + arr[i]
    else:
        sum2 = sum2 + arr[i]

print(max(sum1,sum2))
