class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        ans=[]
        def paths (currpath):
            if n-1==currpath[-1]:
                ans.append(currpath[:])
                return 
            for el in graph [currpath[-1]]:
                currpath.append(el)
                paths(currpath)
                currpath.pop()
        paths([0])
        return ans
