
def getMaxProfit(hier): 
    # The head has no competition and therefore invited 
    totSum = hier[1][0] 
    for i in hier: 
        currentSuperior = hier[i] 
        selectedSub = 0
        # select the subordinate with maximum 
        # value of each superior 
        for j in currentSuperior[1]: 
            if(hier[j][0] > selectedSub): 
                selectedSub = hier[j][0] 
        totSum += selectedSub 
    return totSum 
  
# driver function 
def main(): 
    # Define the Organization as a Dictionary 
    # Index : [Profit, List of Employees] 
        # Same as example 1 given above 
# 1:15 
#       /     \ 
# 2:10    3:12 
#    /   \    /   \ 
# 4:26 5:4 6:7  7:9 
  
    organization = {1:[15, [2, 3]], 
                    2:[10, [4, 5]], 3:[12, [6, 7]], 
                    4:[26, []], 5:[4, []], 6:[7, []], 7:[9, []]} 
    maxProfit = getMaxProfit(organization) 
    print(maxProfit) 
      
main() 
