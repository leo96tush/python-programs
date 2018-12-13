for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sort = sorted(a)
    b_sort = sorted(b)
    a_reverse_sort = a_sort[::-1]
    b_reverse_sort = b_sort[::-1]
    #print(a_sort)
    #print(b_sort)
    #print(a_reverse_sort)
    #print(b_reverse_sort)
    s_1 = 0
    s_2 = 0
    for i in range(len(a)):
        s_1 = s_1 + ( a_sort[i]*b_reverse_sort[i] )
    for i in range(len(a)):
        s_2 = s_2 + ( b_sort[i]*a_reverse_sort[i] )
    print(min(s_1,s_2))
    

    
        
