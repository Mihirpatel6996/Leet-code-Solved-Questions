import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []

        for i in range(len(arr)):
            diff = abs(x - arr[i])

            heapq.heappush(max_heap, (-diff, -arr[i]))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        k_closest_list = sorted([-val for d, val in max_heap])
        return k_closest_list

        

        