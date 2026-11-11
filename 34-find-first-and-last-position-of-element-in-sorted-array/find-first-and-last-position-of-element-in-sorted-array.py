class Solution:
    @staticmethod
    def firstelement(nums: list[int],target:int):
        start =0 
        end = len(nums) -1
        first_ele = -1
        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target :
                first_ele = mid
                end = mid -1
            
            elif nums[mid] < target:
                start = mid +1
            else:
                end = mid -1
        
        return first_ele
    
    @staticmethod
    def lastelement(nums: list[int],target:int):
        start =0 
        end = len(nums) -1
        last_ele = -1
        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target :
                last_ele = mid
                start = mid + 1
            
            elif nums[mid] < target:
                start = mid +1
            else:
                end = mid -1
        
        return last_ele
    
    
                

            
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first_ele = Solution.firstelement(nums,target)
        last_ele = Solution.lastelement(nums,target)

        return [first_ele, last_ele]

        