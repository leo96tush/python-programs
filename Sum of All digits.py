a = input()

while(int(a)>=10):
    a = list(str(a))
    s1 = 0
    for i in range(len(a)):
        s1 = s1 + int(a[i])
    a = s1
        
print(a)
