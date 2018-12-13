rating = list(map(int,input().split()))
candy = [1]*len(rating)
for i in range(len(rating)-1):
    if(rating[i]<rating[i+1]):
        candy[i+1]=candy[i]+1
    elif(rating[i]==rating[i+1]):
        candy[i+1]=candy[i]-1
    else:
        candy[i+1]=candy[i]-1
    
k = min(candy)
if(k<0):
    for i in range(len(candy)):
        candy[i] = candy[i]+(1+(k*(-1)))


print(candy)
