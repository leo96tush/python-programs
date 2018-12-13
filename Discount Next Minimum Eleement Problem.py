n = int(input())
arr = list(map(int,input().split()))
arr.append(0)
discount_amount = []
result_price =[]
j = 1
for i in range(len(arr)):
    while(arr[j]>=arr[i] and j<(len(arr)-1)):
        j = j+1
    
    discount_amount.append(arr[j])
discount_amount.remove(0)
arr.remove(0)
print(*discount_amount,sep=' ')
for i in range(len(arr)):
    result_price.append(arr[i] - discount_amount[i])

print(*result_price,sep=' ')