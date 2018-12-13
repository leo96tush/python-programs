for _ in range(int(input())):
    n = int(input())
    s = 0
    count = 0
    for i in range(2**100):
        if(s>=n):
            break
        else:
            s = s + (2**i)
            count = count + 1
        
    print(count)
