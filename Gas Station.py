def canCompleteCircuit(gas, cost):
        n = len(gas)
        gas_tank = 0
        for i in range(n):
            gas_tank = gas_tank + gas[i%n] - cost[i%n]
            print(gas_tank)
            if(gas_tank<0):
                i = (i+1)%n
            else:
                k = i
        
        #if(gas_tank>=0):
            #print('1')
        #else:
            #print('-1')

        print(k-1)

gas_list = list(map(int,input().split()))
cost_list = list(map(int,input().split()))
canCompleteCircuit(gas_list,cost_list)
