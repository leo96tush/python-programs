def isprime(num):
    for i in range(2,int(num//2)):
        if((num%i) == 0):
            print('NO')
            break
    else:
        print('YES')
    
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    total = 0
    for i in range(len(s)):
        total = total + ord(s[i])

    isprime(total)
