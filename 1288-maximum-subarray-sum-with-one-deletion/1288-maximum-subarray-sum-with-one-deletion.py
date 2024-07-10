class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        pre=[0]*n
        suf=[0]*n
        pre[0]=arr[0]
        suf[n-1]=arr[n-1]
        for i in range(1,n):
            pre[i]=max(arr[i],arr[i]+pre[i-1])
        for i in range(n-2,-1,-1):
            suf[i]=max(arr[i],arr[i]+suf[i+1])
        res=max(pre)
        for i in range(1,n-1):
            res=max(res,pre[i-1]+suf[i+1])
        return res