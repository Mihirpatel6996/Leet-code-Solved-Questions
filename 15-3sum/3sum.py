class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range (0, n-2):
            if(i >0 and nums[i] == nums[i-1]):
                continue
            left = i+1
            right = n-1
            target = nums[i] * -1
            while left<right:
                sum = nums[left]+nums[right]
                if sum == target:
                    sub_list = [nums[i],nums[left],nums[right]]
                    result.append(sub_list)
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right  and nums[right] == nums[right+1]:
                        right-=1
                elif(sum > target):
                    right -=1
                else:
                    left +=1
        return result
                

                
            

        