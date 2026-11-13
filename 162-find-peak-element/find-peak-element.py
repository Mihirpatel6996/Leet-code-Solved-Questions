class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        start = 0
        size  = len(nums)
        end = size-1

        while start <= end:
            mid = start + (end-start)//2

            if mid ==0 :
                return 0 if len(nums) == 1 or nums[0] > nums[1] else 1
            
            if mid == size-1:
                return size-1 if nums[size-1] > nums[size-2] else size-2
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid] < nums[mid+1]:
                start = mid +1
            else:
                end = mid-1

        return 0
            

            
        

        