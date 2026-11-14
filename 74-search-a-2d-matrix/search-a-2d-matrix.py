class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        # treat m x n matrix as sorted array of size m*n
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // n
            c = mid % n
            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

        ## staircase method 
        # rows = len(matrix)
        # cols = len(matrix[0])

        # i = 0
        # j = cols -1

        # while (i>= 0 and i < rows and j >=0 and j < cols):

        #     if matrix[i][j] == target:
        #         return True
        #     elif matrix[i][j] > target:
        #         j -=1
        #     else:
        #         i+=1
        # return False
        