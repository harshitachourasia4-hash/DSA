class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        seen=set()
        left=0
        for ch in range (len(s)):
            while s[ch] in seen and left<=len(s):
                
                seen.remove(s[left])
                left+=1
                
            seen.add(s[ch])
            max_len=max(max_len,ch-left+1)
            
        return max_len

        