class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        start,end=0,m
        half=(m+n+1)//2
        while start<=end:
            i=start+(end-start)//2
            j=half-i
            left_num1=float('-inf') if i==0 else nums1[i-1]
            right_num1=float('inf')if i==m else nums1[i]
            left_nums2=float('-inf') if j==0 else nums2[j-1]
            right_num2=float('inf')if j==n else nums2[j]
            if left_num1<=right_num2 and left_nums2<= right_num1:
                if (m+n)%2==1:
                    return max(left_num1,left_nums2)
                return (max(left_num1,left_nums2)+min(right_num1,right_num2))/2.0
            elif left_nums2> right_num1:
                start=i+1
            else:
                end=i-1
        return 0.0

        