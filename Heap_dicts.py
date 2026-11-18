# heap and dictionaries

def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        from heapq import heappush, heappushpop

        freq = Counter(nums)
        heap = []

        for key, val in freq.items():
            if len(heap) >= k:
                heapq.heappushpop(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        print(heap)
        return [item[1] for item in heap]
