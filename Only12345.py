
for _ in range(int(input())):
    m = input()
    k = int(m)
    c = k
    for i in range(1,c+1):
        r = list(str(i))
        if(('0' in r) or ('6' in r) or ('7' in r) or ('8' in r) or ('9' in r)):
            k = k - 1
    print(k)
