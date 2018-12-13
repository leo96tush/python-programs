for _ in range(int(input())):
    arr = list(input())
    r = list()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i<=j):
                k = arr[i:j]
                count1 = 0
                count2 = 0
                for m in range(len(k)):
                    if(k[m]=='1'):
                        count1=count1+1
                    if(k[m]=='0'):
                        count2=count2+1
                r.append(abs(count2-count1))
    print(max(sorted(set(r))))
            
    
    
