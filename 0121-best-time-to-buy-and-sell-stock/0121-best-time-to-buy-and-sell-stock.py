class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        b=prices[0]
        res=0
        for i in range(1,n):
            if(prices[i]>b):
                res=max(res,prices[i]-b)
            else:
                b=prices[i]
        return res