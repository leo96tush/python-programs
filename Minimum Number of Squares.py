import math
for _ in range(int(input())):
    n = int(input())
    num = n
    count = 0
    while(num>0):
        k = int(math.sqrt(num))
        num = num - pow(k,2)
        count = count+1

    print(count)
