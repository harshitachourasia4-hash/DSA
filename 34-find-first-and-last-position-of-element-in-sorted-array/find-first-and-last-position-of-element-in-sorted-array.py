class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        def check(arr,target,left_or_right):
            st=0
            end=len(arr)-1
            ans=-1
            while st<=end:
                mid=st+(end-st)//2
                if arr[mid]<target:
                    st=mid+1
                elif arr[mid]>target:
                    end=mid-1
                else:
                    ans=mid
                    if left_or_right:
                        end=mid-1
                    else:
                        st=mid+1
            return ans
       

        first=check(arr,target,True)
        second=check(arr,target,False)
        return [first,second]
     





