arr = list(map(int,input().split()))
arr_1 = [1]*len(arr)
lis = list()

for i in range(len(arr)):
    for j in range(len(arr)):
        if(i>j):
            if(arr[i]>arr[j]):
                   arr_1[i]=arr_1[j]+1

print(max(arr_1))
        
    
