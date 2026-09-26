class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        start=0
        end=len(arr)-1
        global ans
        while start<=end:
           
            mid=start+(end-start)//2
            if target>arr[end]:
                ans=end+1
            if arr[mid]==target:
                return mid   
            elif arr[mid]>target:
                ans=mid
                end=mid-1
            else:
                start=mid+1
                
        return ans
             
            
        