class Solution:
    @staticmethod
    def preMaxEle( arr):
        size = len(arr)
        left = []
        max_ele = 0

        for i in range (size):
            max_ele = max(max_ele, arr[i])
            left.append(max_ele)
        
        return left 

    @staticmethod
    def nextMaxEle(arr):
        size = len(arr)
        right = []
        max_ele = 0

        for i in range(size - 1, -1, -1):
            max_ele = max(max_ele, arr[i])
            right.append(max_ele)
        
        return right[::-1]

    def trap(self, height: list[int]) -> int:
        left = Solution.preMaxEle(height)
        right = Solution.nextMaxEle(height)        
        total_water = 0
        for i in range(0,len(height)):
            water = min(right[i], left[i]) - height[i]
            total_water += water
        
        return total_water
        

        