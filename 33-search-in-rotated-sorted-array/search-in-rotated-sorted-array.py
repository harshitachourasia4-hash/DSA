class Solution:
    def search(self, arr: List[int], target: int) -> int:
        start = 0
        end=len(arr)-1
        ans=-1
        while start<=end:
            mid=start+(end-start)//2
            if arr[mid]==target:
                return mid
            if arr[0]<=arr[mid]:
                if arr[0]<=target and target<=arr[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if arr[mid]<target and arr[end]>=target:
                    start=mid+1
                else:
                    end=mid-1
        return ans
                
        
                    
    