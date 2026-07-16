class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res_sum = 0
        max_diff = float('inf')
        for i in range (0, n-2):
            if(i >0 and nums[i] == nums[i-1]):
                continue
            left = i+1
            right = n-1
            while left<right:
                sum = nums[left]+nums[right]+nums[i]
                diff = abs(sum - target)
                if max_diff > diff:
                    max_diff = diff
                    res_sum = sum
                if sum == target:
                    return sum
                elif(sum < target):                    
                    left +=1
                else:
                    right -=1
        return res_sum
        