class Solution:
    def maxSubArray(self, arr: list[int]) -> int:
        current_sum=0
        max_sum=float('-inf')
        for i in range(len(arr)):
            current_sum+=arr[i]
            max_sum=max(max_sum,current_sum)
            if current_sum<0:
                current_sum=0
        return max_sum

