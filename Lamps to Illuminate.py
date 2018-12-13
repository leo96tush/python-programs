def lamps(S):
    count = 0
    for i in range(1,len(S)-1):
        if(S[i-1]=='.' and S[i]=='.' and S[i+1]=='.'):
            count=count+1 
        if(S[i]=='.' and S[i-1]=='.' and S[i+1]=='*' and i==1):
            count = count+1 
        if(S[i]=='.' and S[i-1]=='*' and S[i+1]=='.' and i==len(S)-2):
            count = count+1
        
    return(count)
    
    
    
S = list(input())
print(lamps(S))