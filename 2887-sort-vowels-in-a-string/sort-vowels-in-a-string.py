class Solution:
    def sortVowels(self, s: str) -> str:
        r=list(s)
        rr=""
        for i in range(len(r)):
            if r[i] in "aeiouAEIOU":
                rr+=r[i]
                r[i]="#"
                
        rrr=sorted(rr)
        start=0
        end=0
        while start<len(r):
            if r[start]=="#":
                r[start]=rrr[end]
                end+=1
            start+=1
        return "".join(r)



