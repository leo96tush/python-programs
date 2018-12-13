def numbers(num,digit):
    n = num
    arr = list()
    while(n>0):
        res = n%10
        n = n//10
        if(res==digit):
            return(True)


for _ in range(int(input())):
    num , digit = list(map(int,input().split()))
    arr = list()
    for i in range(0,num+1):
        if(numbers(i,digit)==1):
            arr.append(i)

    if(digit==0):
        arr.insert(0,0)
    if(len(arr)==0):
        arr.append(-1)
    print(*arr,sep=' ')
