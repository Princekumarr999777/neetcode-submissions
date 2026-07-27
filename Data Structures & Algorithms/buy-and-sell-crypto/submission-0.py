class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for i in range(len(prices)):
            curr_ele=prices[i]
            for j in range(i+1,len(prices)):
                if curr_ele<prices[j]:
                    curr_profit=prices[j]-curr_ele
                    max_profit=max(max_profit,curr_profit)
        return max_profit





        