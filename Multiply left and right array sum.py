for _ in range(int(input())):
    n = input()
    arr = list(map(int,input().split()))
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)//2):
        sum1 = sum1+arr[i]
        
    for i in range((len(arr)//2),len(arr)):
        sum2 = sum2+arr[i]

    print(sum1*sum2)
