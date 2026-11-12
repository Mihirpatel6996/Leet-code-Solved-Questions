class Solution:
    @staticmethod
    def BinarySearch(nums:list[int], target:int):
        start =0
        end = len(nums)-1

        while start <= end:
            mid = start+(end-start//2)

            if (nums[mid] == target):
                return mid
            
            if nums[mid] >= nums[start]:
                if(target >= nums[start] and target< nums[mid]):
                    end = mid -1
                else :
                    start = mid+1
            else:
                if (target > nums[mid] and target <= nums[end] ):
                    start = mid+1
                else :
                    end = mid-1
        return -1
                
        
    def search(self, nums: list[int], target: int) -> int:
        index = Solution.BinarySearch(nums, target)
        return index

        