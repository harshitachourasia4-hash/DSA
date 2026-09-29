class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        n=arr.length()
        start=0
        end=n-1
        while start<end:
            mid=start+(end-start)//2
            if arr.get(mid)<arr.get(mid+1):
                start=mid+1
            else:
                end=mid
        peak=start

        start=0
        end=peak
        while start<=end:
            
            mid=start+(end-start)//2
            val=arr.get(mid)
            if val==target:
                return mid
            elif val<target:
                start=mid+1
            else:
                end=mid-1
        start,end=0,n-1
        while start<=end:
            
            mid=start+(end-start)//2
            val=arr.get(mid)
            if val==target:
                return mid
            if val>target:
                start=mid+1
            else:
                end=mid-1
        return -1







        
        