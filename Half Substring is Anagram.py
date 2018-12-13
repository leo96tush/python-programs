str1 = input()
str1 = list(str1.lower())

str2 = list()
str3 = list()
m = 0
if(len(str1)%2==0):
    m = len(str1)//2
else:
    m = 1+len(str1)//2
    
for i in range(m):
    str2.append(str1[i])

for i in range(m,2*m):
    str3.append(str1[i])

if(sorted(str2)==sorted(str3)):
    print(1)
else:
    print(-1)
