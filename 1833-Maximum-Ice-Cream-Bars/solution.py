class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        max_cost=max(costs)
        count=[0]*(max_cost+1)
        for i in costs:
            count[i]+=1
        bar=0
        for i in range(1,max_cost+1):
            if count[i] == 0:
                continue
            if i > coins:
                break
            can_buy=min(count[i],coins//i)
            coins-=can_buy*i
            bar+=can_buy
        return bar
        
