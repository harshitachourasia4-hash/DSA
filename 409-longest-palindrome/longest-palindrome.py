class Solution:
    def longestPalindrome(self, s: str) -> int:
        lower=[0]*26
        upper=26*[0]
        for i in s:
            if ord(i)>=ord('a'):
                lower[ord(i)-ord('a')]+=1
            else:
                upper[ord(i)-ord('A')]+=1
        count=0
        odd=0
        for i in range(26):
            if lower[i]%2==0:
                count+=lower[i]
            else:
                count+=lower[i]-1
                odd=1
            if upper[i]%2==0:
                count+=upper[i]
            else:
                count+=upper[i]-1
                odd=1
        return odd+count

        
