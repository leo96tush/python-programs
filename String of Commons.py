def unique(s):
    res = list()
    for i in s:
        if( i not in res):
            res.append(i)
    return(res)

for _ in range(int(input())):
    string1 = sorted(unique(list(input())))
    string2 = sorted(unique(list(input())))
    result = list()
    for i in string1:
        if( i in string2):
            result.append(i)
    if(len(result)==0):
        print('nil')
    else:
        print(*result,sep='')
