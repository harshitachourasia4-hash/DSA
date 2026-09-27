class Solution:
    def minEatingSpeed(self, arr: List[int], h: int) -> int:
        start=1
        end=max(arr)
        n=len(arr)
        while start<=end:
            mid=start+(end-start)//2
            summ=0
            for i in range(n):
                summ += (arr[i]+mid-1)//mid
            if summ<=h:
                    ans=mid
                    end=mid-1
            else:
                    start=mid+1
        return ans