for _ in range(int(input())):
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        if(arr[i]!=arr[len(arr)-1-i]):
            print("Not Palindrome Array")
            break

    else:
        print("Palindrome Array")
        
    
