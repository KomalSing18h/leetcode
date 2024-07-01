class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range (len(arr)-2):
            p=arr[i]*arr[i+1]*arr[i+2]
            if p%2==1:
                return True
        return False