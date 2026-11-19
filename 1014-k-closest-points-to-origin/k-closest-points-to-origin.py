import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        rows = len(points)
        max_heap = []

        for i in range(0,rows):
            distance = points[i][0]*points[i][0] + points[i][1] *points[i][1]
            heapq.heappush(max_heap, (-distance, (points[i][0],points[i][1])))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        
        points = [point for distance, point in max_heap]
        return points
        


        