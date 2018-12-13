for _ in range(int(input())):
    str1 = list(input())
    str2 = list(input())
    c = list()
    for i in str1:
        if(i not in str2):
            c.append(i)
    for i in str2:
        if(i not in str1):
            c.append(i)
    print(*sorted(set(c)),sep='')
        
