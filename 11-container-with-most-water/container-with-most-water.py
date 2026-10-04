class Solution:
    def maxArea(self, arr: list[int]) -> int:
        start=0
        end=len(arr)-1
        ans=0
        while start<end:
            width=end-start
            height=min(arr[start],arr[end])
            area=height*width
            ans=max(ans,area)
            if arr[start]<arr[end]:
                start+=1
            else:
                 end-=1
        
        return ans
        


            
