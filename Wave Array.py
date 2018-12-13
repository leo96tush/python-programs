for _ in range(int(input())):
    arr = list(map(int,input().split()))
    if( (arr[1]>arr[0] and arr[1]>arr[2]) or (arr[1]<arr[0] and arr[1]<arr[2]) ):
        for i in range(len(arr)//2):
            if( (arr[i+1]>arr[i] and arr[i+2]>arr[i+1]) or (arr[i+1]<arr[i+2] and arr[i]<arr[i+1]) ):
                print("The Array is not a wave array")
                break
            

    else:
        print("The Array is not a wave array")
        
    
