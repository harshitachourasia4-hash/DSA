class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        def binary(arr,target,left_or_right):
            start=0
            end=len(arr)-1
            ans=-1
            
            while start<=end:
               mid=start+(end-start)//2
               if arr[mid]>target:
                   end=mid-1
               elif arr[mid]<target:
                   start=mid+1
               else:
                    ans=mid
                    if left_or_right:
                        end=mid-1
                    else:
                        start=mid+1
            return ans
            
        first=binary(arr,target,True)
        secondary=binary(arr,target,False)
        return [first,secondary]

             
