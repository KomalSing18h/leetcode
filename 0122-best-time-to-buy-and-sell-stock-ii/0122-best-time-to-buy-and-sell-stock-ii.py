class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        prof=0
        maxi=prices[0]
        mini=prices[0]
        for i in range(1,n):
            if (prices[i]>=maxi):
                maxi=prices[i]
            else:
                prof=prof+(maxi-mini)
                maxi=prices[i]
                mini=prices[i]
        return(prof+maxi-mini)

