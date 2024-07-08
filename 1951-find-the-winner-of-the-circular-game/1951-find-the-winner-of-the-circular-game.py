class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a=0
        for i in range(2,n+1):
            a=(a+k)%i
        return a+1

