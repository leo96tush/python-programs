def StringMatch(S):
    lo = 0
    hi = len(S)
    my_list = list()
    for x in S:
        if x == 'I':
            my_list.append(lo)
            lo = lo+1
        else:
            my_list.append(hi)
            hi = hi-1
    return(my_list+[lo])

S = list(input())
print(StringMatch(S))