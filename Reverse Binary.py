def decimalToBinary(n): 
    return(bin(n).replace("0b",""))

def binaryToDecimal(n):
    k = ''.join(n)
    return(int(k,2))

for _ in range(int(input())):
    n = int(input())
    k = list(decimalToBinary(n))
    m = k[::-1]
    print(binaryToDecimal(m))
            
    
