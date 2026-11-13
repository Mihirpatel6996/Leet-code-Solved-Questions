class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height) -1
        max_fill = float('-inf')

        while(start <= end):
            length = min(height[start], height[end])
            area = length * (end-start)
            max_fill = max(max_fill, area)

            if(height[start] <= height[end]):
                start += 1
            else:
                end -=1
        
        return max_fill
        