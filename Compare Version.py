arr1 = list(map(str,input()))
arr2 = list(map(str,input()))

if(len(arr1)==len(arr2)):
    pass
elif(len(arr1)>len(arr2)):
    for i in range(len(arr1)-len(arr2)):
        arr2.append(' ')
else:
    for i in range(len(arr2)-len(arr1)):
        arr1.append(' ')
print(arr1)
print(arr2)


for i in range(max(len(arr1),len(arr2))):
    if(ord(arr1[i])==ord(arr2[i])):
        pass
    elif(ord(arr1[i])>ord(arr2[i])):
        print('1')
        break
    elif(ord(arr2[i])>ord(arr1[i])):
        print('-1')
        break
    else:
        pass


