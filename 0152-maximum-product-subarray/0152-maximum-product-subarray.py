class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        minp,maxp=1,1
        for n in nums:
            if n==0:
                minp,maxp=1,1
                continue
            t=maxp*n
            maxp=max(n*maxp,n*minp,n)
            minp=min(t,n*minp,n)
            res=max(res,maxp)
        return res