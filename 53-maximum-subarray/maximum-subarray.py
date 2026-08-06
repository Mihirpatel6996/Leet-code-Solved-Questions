class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0 
        ans_start = -1
        ans_end = -1

        for i in range(0, len(nums)):
            if current_sum == 0:
                start = i
            current_sum += nums[i]
            #  max_sum = max(max_sum, current_sum) instead of this
            if(current_sum > max_sum):
                max_sum = current_sum
                ans_start = start 
                ans_end = i
            if(current_sum < 0):
                current_sum = 0 
        return max_sum
       

        
        