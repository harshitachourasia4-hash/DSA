class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums,target,is_left):
            start,end=0,len(nums)-1
            indx=-1
            while start<=end:
                mid=start+(end-start)//2
                if nums[mid]<target:
                    start=mid+1
                elif nums[mid]>target:
                    end=mid-1
                else:
                    indx=mid
                    if is_left:
                        end=mid-1
                    else:
                        start=mid+1
            return indx
        left=binary_search(nums,target,True)
        right=binary_search(nums,target,False)
        return [left,right]
            