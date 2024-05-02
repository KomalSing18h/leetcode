class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r,c=len(image),len(image[0])
        newColor=image[sr][sc]
        if newColor==color:
            return image
        def dfs(R,C):
            if image[R][C]==newColor:
               image[R][C]=color 
               if R>=1:
                dfs(R-1,C)
               if R+1<r:
                dfs(R+1,C)
               if C>=1:
                dfs(R,C-1)
               if C+1<c:
                dfs(R,C+1)
        dfs(sr,sc)
        return image 



