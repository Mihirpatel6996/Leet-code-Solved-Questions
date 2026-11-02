from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        queue = deque() 
        i=0
        j=0
        while (j < len(nums)):
            while queue and queue[-1] < nums[j]:
                queue.pop()
            
            queue.append(nums[j])
            
            if (j-i+1 == k):
                result.append(queue[0])

                if queue and queue[0] == nums[i]:
                    queue.popleft()
                
                i+=1
            
            j+=1
        
        return result
