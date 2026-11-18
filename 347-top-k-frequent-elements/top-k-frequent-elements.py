import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        min_heap=[]
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) +1

        for value,frequency in freq.items():
            heapq.heappush(min_heap, (frequency, value))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        k_top = sorted([val for d, val in min_heap])    
        return k_top


        

        