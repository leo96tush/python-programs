def decimalToBinary(n): 
    return bin(n).replace("0b","")

for _ in range(int(input())):
    n = int(input())
    k = list(decimalToBinary(n))
    s = 0
    for i in range(len(k)):
        for j in range(len(k)):
            if(i<j):
                s = s + 2*(int(k[i])) + int(k[j])

    print(s)
            
    
