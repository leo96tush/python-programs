def all_edges(arr):
    arr_1 = list()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i<j):
                m = arr[i]+arr[j]
                arr_1.append(m)
    return(set(sorted(arr_1)))
    
    
arr = list(input().split())
print(all_edges(arr))
