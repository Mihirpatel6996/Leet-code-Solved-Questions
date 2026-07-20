class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0,0
        n = len(nums)
        min_count = float('inf')
        window_sum = 0

        for right in range(n):
            window_sum += nums[right]

            while (window_sum>= target):
                window_length = right-left+1
                min_count = min(min_count, window_length)
                window_sum -= nums[left]
                left +=1
        return 0 if min_count == float('inf')else min_count

        