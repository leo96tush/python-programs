import sys
sys.setrecursionlimit(1500)

        
def bigger_palindrome(num):
    arr=[]
    n = num
    while(n>0):
        arr.append(n%10)
        n = n//10
    if(arr == arr[::-1]):
        return(num)
    else:
        return(bigger_palindrome(num+1))

def smaller_palindrome(num):
    arr=[]
    n = num
    while(n>0):
        arr.append(n%10)
        n = n//10
    if(arr == arr[::-1]):
        return(num)
    else:
        return(smaller_palindrome(num-1))
    
for _ in range(int(input())):
    n = int(input())
    k=bigger_palindrome(n)
    m=smaller_palindrome(n)
    if((k-n)>=(n-m)):
        print(m)
    else:
        print(k)


    
    


