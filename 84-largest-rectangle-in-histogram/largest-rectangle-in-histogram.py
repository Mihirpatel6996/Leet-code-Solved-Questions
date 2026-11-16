class Solution:
    @staticmethod
    def getNSL(heights):
        n = len(heights)
        left = [-1] * n
        stack = [] # store index
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            # else left[i] stays -1
            stack.append(i)
        return left

    @staticmethod
    def getNSR(heights):
        n = len(heights)
        right = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        return right
    def largestRectangleArea(self, heights: list[int]) -> int:
        left = Solution.getNSL(heights)
        right = Solution.getNSR(heights)
        max_area = 0
        for i in range(len(heights)):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        
        return max_area
        