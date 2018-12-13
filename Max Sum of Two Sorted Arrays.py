arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
n = int(input())
arr1_sort = sorted(arr1)
arr1_sort = arr1_sort[::-1]
arr2_sort = sorted(arr2)
arr2_sort = arr2_sort[::-1]

print(arr1_sort)
print(arr2_sort)


c = list()
c.append(arr1_sort[0]+arr2_sort[0])
i = 0
j = 0
while(len(c)<=n):
    t = max(arr1_sort[i]+arr2_sort[j+1],arr1_sort[i+1]+arr2_sort[j])
    c.append(t)
    if(arr1_sort[i]+arr2_sort[j+1]==arr1_sort[i+1]+arr2_sort[j]):
        c.append(t)
    else:
        if(t == arr1_sort[i]+arr2_sort[j+1]):
            j = j+1
        elif(t == arr1_sort[i+1]+arr2_sort[j]):
            i = i+1
            
print(*sorted(c),sep=' ')
