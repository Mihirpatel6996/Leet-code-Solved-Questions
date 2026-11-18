from collections import Counter
import heapq

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        min_heap = []
        solution =[]

        for value, frequency in freq.items():
            heapq.heappush(min_heap,(frequency, -value))
        
        while min_heap:
            frequency, neg_value = heapq.heappop(min_heap)
            solution.extend([-neg_value] * frequency)

        return solution



        