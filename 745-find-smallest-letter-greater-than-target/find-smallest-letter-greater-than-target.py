class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        start, end = 0, len(letters) -1
        index = -1
        while (start <= end):
            mid = start + (end-start)//2

            if (letters[mid] <= target):
                start = mid+1
            elif(letters[mid] > target):
                index = mid
                end = mid - 1
        if index == -1:
            return letters[0]
        
        return letters[index]

        