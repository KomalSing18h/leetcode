class Solution:
    def minimumDeletions(self, s: str) -> int:
        ac=0
        for c in s:
            ac+=1 if c=="a" else 0
        bc=0
        res=len(s)
        for i,c in enumerate(s):
            if c=="a":
                ac-=1
            res=min(res,bc+ac)
            if c=="b":
                bc+=1
        return res